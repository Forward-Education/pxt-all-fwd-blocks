# This script specifically updates all "fwd-*" dependencies to the provided version or commit.

import json
import os
import sys
from typing import Dict, Any

def find_and_update_pxt_files(new_version: str, prefix: str = "fwd-") -> None:
    """
    Finds all pxt.json files in the current directory and its subdirectories
    and updates dependencies that start with the specified prefix,
    always ensuring a trailing newline.
    """
    start_directory = "."  # Always start from the current directory
    print(f"Searching for pxt.json files in '{start_directory}' and its subdirectories...")
    found_files = False

    for root, _, files in os.walk(start_directory):
        for file in files:
            if file == "pxt.json":
                found_files = True
                file_path = os.path.join(root, file)
                print(f"\nProcessing: {file_path}")

                try:
                    with open(file_path, "r+") as f:
                        content: Dict[str, Any] = json.load(f)
                        updated_any_dependency = False

                        if "dependencies" in content:
                            dependencies_to_update = [
                                dep_name
                                for dep_name in content["dependencies"]
                                if dep_name.startswith(prefix)
                            ]

                            if not dependencies_to_update:
                                print(f"  No dependencies starting with '{prefix}' found in '{file_path}'")
                                # Even if no relevant dependencies, ensure trailing newline
                                f.seek(0)
                                current_file_content = f.read()
                                if not current_file_content.endswith('\n'):
                                    f.seek(0, os.SEEK_END) # Go to end of file
                                    f.write('\n')
                                continue

                            for dependency_name in dependencies_to_update:
                                current_dependency_url: str = content["dependencies"][dependency_name]

                                if not current_dependency_url.startswith("github:"):
                                    print(f"  Skipping '{dependency_name}' in '{file_path}': Not a GitHub dependency URL.")
                                    continue

                                parts = current_dependency_url.split("#")
                                base_url = parts[0] if len(parts) > 1 else current_dependency_url
                                updated_dependency_url = f"{base_url}#{new_version}"

                                if updated_dependency_url != current_dependency_url:
                                    content["dependencies"][dependency_name] = updated_dependency_url
                                    updated_any_dependency = True
                                    print(
                                        f"  Updated '{dependency_name}' in '{file_path}' to '{new_version}'"
                                    )
                                else:
                                    print(
                                        f"  '{dependency_name}' in '{file_path}' is already at '{new_version}'"
                                    )
                            
                            if updated_any_dependency:
                                f.seek(0)  # Rewind to the beginning
                                json.dump(content, f, indent=4)
                                f.write('\n') # Always add a trailing newline
                                f.truncate() # Truncate any remaining old content
                            else:
                                # If no dependencies were updated but the file was loaded,
                                # ensure it still ends with a newline if it doesn't already.
                                f.seek(0)
                                current_file_content = f.read()
                                if not current_file_content.endswith('\n'):
                                    f.seek(0, os.SEEK_END) # Go to end of file
                                    f.write('\n')

                        else:
                            print(f"  No 'dependencies' section found in '{file_path}'")
                            # If no dependencies section, ensure it still ends with a newline
                            f.seek(0)
                            current_file_content = f.read()
                            if not current_file_content.endswith('\n'):
                                f.seek(0, os.SEEK_END) # Go to end of file
                                f.write('\n')


                except FileNotFoundError:
                    print(f"Error: File not found at {file_path}")
                except json.JSONDecodeError:
                    print(f"Error: Could not decode JSON from {file_path}. Is it a valid JSON file?")
                except Exception as e:
                    print(f"An unexpected error occurred while processing {file_path}: {e}")

    if not found_files:
        print(f"No 'pxt.json' files found in '{start_directory}' or its subdirectories.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update-dependencies.py <new_version>")
        print("Example: python update-dependencies.py v1.0.2")
        sys.exit(1)

    NEW_DEPENDENCY_VERSION = sys.argv[1]
    
    # The prefix for dependencies to update is now hardcoded as 'fwd-'
    find_and_update_pxt_files(NEW_DEPENDENCY_VERSION, prefix="fwd-")

    print("\nScript finished.")
