fwdButtons.dial1.onRotated(
    fwdEnums.ClockwiseCounterclockwise.Clockwise,
    function () {
        basic.showNumber(fwdButtons.dial1.position())
    },
)
fwdSensors.line1.onLineSensorStateChange(function () {
    if (fwdSensors.line1.isLineSensorState(fwdEnums.OnOff.Off)) {
        basic.showNumber(fwdSensors.line1.lineSensorState())
    }
})
fwdButtons.dialButton1.onEvent(jacdac.ButtonEvent.Down, function () {
    if (fwdButtons.dialButton1.isPressed()) {
        basic.showNumber(fwdButtons.dialButton1.holdDuration())
    }
})
fwdButtons.touch1.onEvent(jacdac.ButtonEvent.Down, function () {
    if (fwdButtons.touch1.isPressed()) {
        basic.showNumber(fwdButtons.touch1.holdDuration())
    }
})
fwdSensors.float1.onFloatChange(fwdEnums.RaisedLowered.Raised, function () {
    if (
        fwdSensors.float1.floatStateConditional(fwdEnums.RaisedLowered.Raised)
    ) {
        basic.showNumber(fwdSensors.float1.floatState())
    }
})
fwdButtons.BTN1.onEvent(jacdac.ButtonEvent.Down, function () {
    if (fwdButtons.BTN1.isPressed()) {
        basic.showNumber(fwdButtons.BTN1.holdDuration())
    }
})
if (fwdSensors.current1.isPastThreshold(0, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.current1.current())
}
if (fwdSensors.voltage1.isPastThreshold(0, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.voltage1.voltage())
}
fwdSensors.ph1.calibrate(0, 0, 0, 0)
if (fwdSensors.ph1.isPastThreshold(0, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.ph1.ph())
}
if (fwdSensors.solar1.isPastThreshold(5, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.solar1.lightLevel())
}
if (fwdSensors.sonar1.isPastThreshold(0, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.sonar1.distance())
}
if (fwdSensors.temperature1.isPastThreshold(0, fwdEnums.OverUnder.Over)) {
    basic.showNumber(fwdSensors.temperature1.temperature())
}
if (fwdMotors.pump.isOn()) {
    fwdMotors.pump.timedRun(500)
    fwdMotors.pump.setOn(false)
}
fwdMotors.setSpeed(fwdBase.leftServo, 0)
basic.showNumber(fwdMotors.getSpeed(fwdBase.leftServo))
fwdMotors.setupDriving(fwdBase.leftServo, fwdBase.leftServo)
fwdMotors.drive(50, 50, 1000)
fwdMotors.setAngle(fwdBase.leftServo, 90)
fwdMotors.setAngleAndWait(fwdBase.leftServo, 0)
basic.showNumber(fwdMotors.getAngle(fwdBase.leftServo))
fwdLights.ledRing1.setPixelColor(fwdLights.LEDRingPixels.Pixel1, 0xff0000)
fwdLights.ledRing1.setAllPixelsColor(0xff0000)
fwdLights.ledRing1.setBrightness(10)
fwdLights.ledRing1.rotate(1)
fwdLights.ledRing1.shift(1)
basic.showNumber(fwdLights.ledRing1.brightness())
