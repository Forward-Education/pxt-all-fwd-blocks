import os
import json
import subprocess
import glob
import shutil

# --- Configuration ---
PXT_JSON_PATH = 'pxt.json'  # Path to your pxt.json file
TESTS_DIR = 'tests'         # Directory containing your test TypeScript files
MKC_COMMAND = 'mkc'         # The command to execute (e.g., 'mkc', 'npm run build', etc.)

def find_ts_files(directory):
    """
    Recursively finds all TypeScript files (.ts) in the given directory.

    Args:
        directory (str): The path to the directory to search.

    Returns:
        list: A list of absolute paths to .ts files.
    """
    ts_files = []
    # Use glob to find all .ts files recursively
    # os.path.join is used to ensure cross-platform compatibility for paths
    search_pattern = os.path.join(directory, '**', '*.ts')
    for file_path in glob.glob(search_pattern, recursive=True):
        ts_files.append(file_path)
    return ts_files

def read_pxt_json(file_path):
    """
    Reads the pxt.json file.

    Args:
        file_path (str): The path to the pxt.json file.

    Returns:
        dict: The parsed JSON content of the pxt.json file.

    Raises:
        FileNotFoundError: If pxt.json does not exist.
        json.JSONDecodeError: If pxt.json is not valid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: {file_path} not found.")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error parsing {file_path}: {e}", e.doc, e.pos)

def write_pxt_json(file_path, data):
    """
    Writes the given data back to the pxt.json file.

    Args:
        file_path (str): The path to the pxt.json file.
        data (dict): The dictionary to write as JSON.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        f.write('\n') # Ensure the file ends with a newline

def run_mkc_command():
    """
    Executes the mkc command in the current working directory.
    Uses shell=True to allow the system's PATH to be used, which can resolve
    "command not found" issues if the command is accessible in the terminal
    but not directly in the script's environment.
    """
    print(f"\n--- Running command: {MKC_COMMAND} ---")
    try:
        # Using subprocess.run for better control over output and error handling
        # capture_output=True captures stdout and stderr
        # text=True decodes stdout/stderr as text
        # check=True raises CalledProcessError if the command returns a non-zero exit code
        # shell=True allows the command to be executed through the shell,
        # which can help find commands in the system's PATH.
        result = subprocess.run(
            MKC_COMMAND, # Pass command as a single string when shell=True
            capture_output=True,
            text=True,
            check=True,
            shell=True # Key change: Run through the shell
        )
        print("Command output:")
        print(result.stdout)
        if result.stderr:
            print("Command errors (stderr):")
            print(result.stderr)
        print("Command executed successfully.")
        return True
    except FileNotFoundError:
        print(f"Error: Command '{MKC_COMMAND}' not found. "
              "Please ensure it's installed and in your system's PATH.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{MKC_COMMAND}' failed with exit code {e.returncode}")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        return False
    except Exception as e:
        print(f"An unexpected error occurred while running '{MKC_COMMAND}': {e}")
        return False

def main():
    """
    Main function to orchestrate the test execution.
    """
    original_pxt_content = None
    failed_tests = [] # List to store paths of tests that fail mkc command
    try:
        # 1. Read and backup the original pxt.json content
        print(f"Reading original {PXT_JSON_PATH}...")
        original_pxt_content = read_pxt_json(PXT_JSON_PATH)
        print("Original pxt.json backed up.")

        # 2. Find all TypeScript test files
        print(f"Searching for .ts files in '{TESTS_DIR}' directory...")
        ts_files = find_ts_files(TESTS_DIR)

        if not ts_files:
            print(f"No .ts files found in '{TESTS_DIR}'. Exiting.")
            return

        print(f"Found {len(ts_files)} TypeScript test files:")
        for ts_file in ts_files:
            print(f"  - {ts_file}")

        # 3. Process each test file
        for i, test_file_path in enumerate(ts_files):
            print(f"\n--- Processing test file {i+1}/{len(ts_files)}: {test_file_path} ---")

            # Get the relative path for pxt.json
            # This logic assumes pxt.json is in the current working directory,
            # and test files are relative to it.
            relative_test_path = os.path.relpath(test_file_path, os.path.dirname(PXT_JSON_PATH))
            # Normalize path separators to forward slashes for consistency with JSON/web paths
            relative_test_path = relative_test_path.replace(os.path.sep, '/')

            # Modify pxt.json
            current_pxt_content = original_pxt_content.copy() # Make a copy to avoid modifying backup
            current_pxt_content['testFiles'] = [relative_test_path]
            print(f"Updating '{PXT_JSON_PATH}' with testFiles: {current_pxt_content['testFiles']}")
            write_pxt_json(PXT_JSON_PATH, current_pxt_content)

            # Run mkc command
            success = run_mkc_command()
            if not success:
                print(f"Warning: Command '{MKC_COMMAND}' failed for {test_file_path}. Continuing to next test.")
                failed_tests.append(test_file_path) # Add to failed list
            else:
                print(f"Successfully ran '{MKC_COMMAND}' for {test_file_path}.")

        # 4. Report summary of failed tests
        if failed_tests:
            print("\n--- Summary of Failed Tests ---")
            for failed_test in failed_tests:
                print(f"  - {failed_test}")
            print("-------------------------------\n")
        else:
            print("\nAll tests passed successfully (mkc returned 'Build OK').")


    except FileNotFoundError as e:
        print(e)
    except json.JSONDecodeError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # 5. Restore the original pxt.json
        if original_pxt_content:
            print(f"\nRestoring original {PXT_JSON_PATH}...")
            write_pxt_json(PXT_JSON_PATH, original_pxt_content)
            print("Original pxt.json restored successfully.")
        else:
            print("\nNo original pxt.json content to restore.")

if __name__ == "__main__":
    main()
