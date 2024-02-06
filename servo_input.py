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

def servo_func(angle):
    # by experimentation
    duty_180deg = 11.5
    duty_0deg = 2.5
    
    duty = ((duty_180deg-duty_0deg)/180)*angle + duty_0deg
    print("duty:", duty)
    p.ChangeDutyCycle(duty)
    
try:
    while True:
        input_angle = ""
        while input_angle == "":
            input_angle = input("What is your angle in degrees?")
            
            #takes in angle +-1 deg, as servo is not that precise anyways
            if not input_angle.isnumber() or int(input_angle) < 0 or int(input_angle) > 180:
                print("invalid input")
                break
            
            servo_func(int(input_angle))
            print("input_angle:", int(input_angle))
            time.sleep(0.3)
                
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()