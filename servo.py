# EG2310
# This code is used to control the servo
# Students will be given this code but will need to understand how it works
# Additional h/w exercise is to write a function to turn the servo by an angle
# The servo motor may be chosen to tilt the payload

import time
import RPi.GPIO as GPIO

# Set pin numbering convention
GPIO.setmode (GPIO.BCM) # PWM GPIO12
             
# Choose an appropriate pwm channel to be used to control the servo
servo_pin = 12

# Set the pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Initialise the servo to be controlled by pwm with 50 Hz frequency
p = GPIO.PWM(servo_pin, 50)

# Set servo to 90 degrees as it's starting position
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5) #90 deg position
        print("90 deg")
        time.sleep(1) #delay 1 second
        p.ChangeDutyCycle(2.5) #0 deg position
        print("0 deg")
        time.sleep(1) #delay 1 second again
        p.ChangeDutyCycle(12.5) #180 deg position
        print("180 deg")
        time.sleep(1) #delay 1 second again... ...
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()