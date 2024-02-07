# EG2310
# This code is used to control the servo
# Students will be given this code but will need to understand how it works
# Additional h/w exercise is to write a function to turn the servo by an angle
# The servo motor may be chosen to tilt the payload

import time
import RPi.GPIO as GPIO

# Set pin numbering convention
GPIO.setmode(GPIO.BCM)  # PWM GPIO12

# Choose an appropriate pwm channel to be used to control the servo
servo_pin = 12

# Set the pin as an output
GPIO.setup(servo_pin, GPIO.OUT)

# Initialise the servo to be controlled by pwm with 50 Hz frequency
p = GPIO.PWM(servo_pin, 50)

# Set servo to 90 degrees as it's starting position
p.start(7.5)


def servo_func(angle):
    # by experimentation
    duty_180deg = 11.5
    duty_0deg = 2.5

    duty = ((duty_180deg - duty_0deg) / 180) * angle + duty_0deg
    print("duty:", duty)
    p.ChangeDutyCycle(duty)


# If the given input is valid (integer between 0 and 180), returns the value as int.
# Otherwise, return -1.
def to_integer(input_str):
    # Invalid if not an integer
    if not input_str.isnumeric():
        return -1

    value = int(input_str)

    # Invalid if not in [0, 180]
    if value < 0 or value > 180:
        return -1

    return value


try:
    while True:
        input_str = input("What is your angle in degrees?")

        angle = to_integer(input_str)

        # if angle is -1, it means that the input is invalid
        if angle == -1:
            continue

        print("input_angle:", angle)

        # set servo to the designated angle
        servo_func(angle)
        time.sleep(0.3)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
