hummingbird.start_hummingbird()
distance = 0

def on_forever():
    global distance
    #get distance from sensor 
    #NOTE: use a large & hard surfaced object infront of the distance sensor
    #soft "squishy" materials will absorb the sensor ping and give bad results
    distance = hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.ONE)
    #too close, light up red LED
    if distance > 5 and distance < 15:
        hummingbird.set_tri_led(TwoPort.ONE, 100, 0, 0)
    #middle distance, light up green LED
    elif distance >= 15 and distance <30:
        hummingbird.set_tri_led(TwoPort.ONE, 0, 100, 0)
    #far distance, light up blue LED
    else:
        hummingbird.set_tri_led(TwoPort.ONE, 0, 0, 100)
forever(on_forever)