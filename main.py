let strip: neopixel.Strip = null
let Password = 0
basic.forever(function () {
    strip = neopixel.create(DigitalPin.P3, 7, NeoPixelMode.RGB)
    if (pins.digitalReadPin(DigitalPin.P1) == 1) {
        basic.pause(1000)
        music.play(music.createSoundExpression(WaveShape.Square, 1600, 1, 255, 255, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(2000)
        pins.servoWritePin(AnalogPin.P2, 180)
    }
    if (pins.analogReadPin(AnalogPin.P0) == 1) {
        Password = 1
    } else if (pins.analogReadPin(AnalogPin.P0) == 2) {
        Password = 2
    } else if (pins.analogReadPin(AnalogPin.P0) == 3) {
        Password = 3
    } else if (pins.analogReadPin(AnalogPin.P0) == 4) {
        Password = 4
    } else if (pins.analogReadPin(AnalogPin.P0) == 5) {
        Password = 5
    } else {
        Password = 0
    }
})
