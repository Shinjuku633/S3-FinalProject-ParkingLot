let Password = 0
basic.forever(function () {
    Password = pins.map(
    pins.analogReadPin(AnalogPin.P0),
    1,
    1023,
    1,
    5
    )
    Password = Math.round(Password)
    basic.showNumber(Password)
})
