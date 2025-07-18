// This extension is quite big to write comprehensive tests for. Here are some compilation tests to start.
// It already has coverage via the individual kit extensions.
// Any multi-kit tutorials will be hosted here and the final code for those tutorials will be added as test files

// lights tests
// setBrightness(value: number)
basic.forever(() => {
    console.log("Test Start")
    console.log(
        "The brightness is changing every second for 6 seconds, but the Jacdac simulator only shows on / off."
    )
    basic.pause(1000)
    fwdLights.lights1.setBrightness(100)
    console.log("Light on? " + fwdLights.lights1.isOn())
    basic.pause(1000)
    fwdLights.lights1.setBrightness(75)
    basic.pause(1000)
    fwdLights.lights1.setBrightness(50)
    basic.pause(1000)
    fwdLights.lights1.setBrightness(25)
    basic.pause(1000)
    fwdLights.lights1.setBrightness(10)
    basic.pause(1000)
    fwdLights.lights1.setBrightness(0)
    console.log("Light on? " + fwdLights.lights1.isOn())
    console.log("Test End")
})
fwdSensors.float1.onFloatChange(fwdEnums.RaisedLowered.Raised, () => {
    console.log("Event: raised")
})
fwdSensors.float1.onFloatChange(fwdEnums.RaisedLowered.Lowered, () => {
    console.log("Event: lowered")
})
basic.forever(() => {
    if (
        fwdSensors.float1.floatStateConditional(fwdEnums.RaisedLowered.Raised)
    ) {
        console.log("State: " + fwdSensors.float1.floatState())
    }
    if (
        fwdSensors.float1.floatStateConditional(fwdEnums.RaisedLowered.Lowered)
    ) {
        console.log("State: " + fwdSensors.float1.floatState())
    }
    basic.pause(1000)
})

// dial tests
// position()
// onRotated(direction: DialDirection, handler: () => void): void
fwdButtons.dial1.onRotated(fwdEnums.ClockwiseCounterclockwise.Clockwise, () =>
    console.log("turned -> position " + fwdButtons.dial1.position())
)
fwdButtons.dial1.onRotated(
    fwdEnums.ClockwiseCounterclockwise.Counterclockwise,
    () => console.log("turned <- position " + +fwdButtons.dial1.position())
)

// button tests
// onEvent(event: jacdac.ButtonEvent, handler: () => void)
// holdDuration(): number
// isPressed(): boolean
console.log("Button pressed? " + fwdButtons.dialButton1.isPressed())
fwdButtons.dialButton1.onEvent(jacdac.ButtonEvent.Down, () =>
    console.log("dialdown")
)
fwdButtons.dialButton1.onEvent(jacdac.ButtonEvent.Up, () =>
    console.log("dialup")
)
fwdButtons.dialButton1.onEvent(jacdac.ButtonEvent.Hold, () =>
    console.log("Hold Duration: " + fwdButtons.dialButton1.holdDuration())
)
