hummingbird.startHummingbird()
let distance = 0
forever(function on_forever() {
    
    // get distance from sensor 
    // NOTE: use a large & hard surfaced object infront of the distance sensor
    // soft "squishy" materials will absorb the sensor ping and give bad results
    distance = hummingbird.getSensor(SensorType.Distance, ThreePort.One)
    // too close, light up red LED
    if (distance > 5 && distance < 15) {
        hummingbird.setTriLED(TwoPort.One, 100, 0, 0)
    } else if (distance >= 15 && distance < 30) {
        // middle distance, light up green LED
        hummingbird.setTriLED(TwoPort.One, 0, 100, 0)
    } else {
        // far distance, light up blue LED
        hummingbird.setTriLED(TwoPort.One, 0, 0, 100)
    }
    
})
