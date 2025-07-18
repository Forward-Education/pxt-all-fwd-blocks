# all-fwd-blocks

The full library of blocks supporting Forward Education's Jacdac modules. Combine kits to unlock new possibilities. Find us at [forwardedu.com](https://forwardedu.com/) and [learn.forwardedu.com](https://learn.forwardedu.com/).

This extension supports the following products:

-   [Climate Action Kit](https://forwardedu.com/pages/climate-action-kit)
-   [Smart Solar Energy Kit](https://forwardedu.com/products/smart-solar-energy-kit)
-   [Smart Soldering Kit](https://forwardedu.com/products/smart-learn-to-solder-kit)
-   [Smart Hydroponics Kit](https://forwardedu.com/products/smart-hydroponics-kit)

### ~ reminder

![works with micro:bit V2 only image](/static/v2/v2-only.png)

These blocks require the [micro:bit V2](/device/v2). If you use them with a V1 micro:bit you will see the 927 error code on the screen.

### ~

## Example Usage

Our learning systems are designed to simplify teaching coding and computer science for educators at all experience levels.
Our kits can be used on their own or joined with other kits to access a larger library of sensors, motors, lights, and buttons.
Check out our libraries of [lessons](https://learn.forwardedu.com/lesson-library), [projects](https://learn.forwardedu.com/projects/), and [tutorials](https://learn.forwardedu.com/tutorials/). Samples of coding with combined kits are found below.

The Smart Solar Energy Kit provides the tools to monitor and optimize solar energy production. Imagine you are running an experiment and need to collect current and voltage data under consistent conditions using the [datalogger extension](https://makecode.microbit.org/reference/datalogger). If something gets near the solar panel it might cast shade on it, affecting the data quality. Using the sonar sensor from the Climate Action Kit you can detect if there is an object near the solar panel. That way if there is a nearby object detection you can choose whether or not to include the energy data at that point. You could get a more complete picture with multiple sonar sensors pointing in different directions. Optionally, add an audible obstruction alarm using micro:bit music blocks that trigger during object detections.

```package
datalogger
```

```blocks
datalogger.setColumnTitles(
"sonar",
"current",
"voltage"
)
basic.showNumber(fwdSensors.current1.current())
basic.showNumber(fwdSensors.voltage1.voltage())
basic.showNumber(fwdSensors.sonar1.fwdDistance())
loops.everyInterval(1000, function () {
    datalogger.log(datalogger.createCV("sonar", fwdSensors.sonar1.fwdDistance()))
    datalogger.log(datalogger.createCV("current", fwdSensors.current1.current()))
    datalogger.log(datalogger.createCV("voltage", fwdSensors.voltage1.voltage()))
})
```

The Smart Hydroponics Kit has a light that is used to grow vegetables. We can use components from the Climate Action Kit and Smart Solar Energy Kit to characterize the light's brightness. For example, how much brighter is the light at the center vs the sides? How much does brightness decrease with distance from the light? We can use the solar panel voltage generation and solar sensor to estimate brightness.

For this exercise it's simplest to use the MakeCode website's "Devices" view for real-time, easy-to-read measurements. In order to ensure the the "Devices" view appears and populates we simply need to have a block for each of our sensors in "on start", and the program downloaded to the micro:bit. Then with your breakout board turned on and sensors plugged in you can start moving things around and seeing how the measurements change live in your web browser. You can even manually change the light's brightness setting in "Devices" view.

```blocks
fwdLights.lights1.setBrightness(100)
basic.showNumber(fwdSensors.solar1.lightLevel())
basic.showNumber(fwdSensors.voltage1.voltage())
```

## Supported Targets

-   for PXT/microbit

## License

MIT
