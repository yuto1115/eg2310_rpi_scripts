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
    #Position "0" (1.5 ms pulse) is middle, "90" (~2ms pulse) is middle, is all the 
    # way to the right, "-90" (~1ms pulse) is all the way to the left
    # 1.5ms/20ms    = 7.5%  90 deg
    # 2ms/20ms      = 10%   180 deg
    # 1ms/20ms      = 5%    0deg
    # assume linear
    
    # datasheet is shit idk
    
    # 7.5%  90 deg
    # 12.5% 180 deg
    # 2.5%  0deg
    # assume linear
    
    duty = ((12.5-2.5)/180)*angle + 2.5
    print("duty:", duty)
    p.ChangeDutyCycle(duty)
    
try:
    while True:
        input_angle = ""
        while input_angle == "":
            input_angle = input("What is your angle in degrees?")
            
            if not input_angle.isdigit() or int(input_angle) < 0 or int(input_angle) > 180:
                print("invalid input")
                break
            
            servo_func(int(input_angle))
            print("input_angle:", int(input_angle))
            time.sleep(0.3)
                
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()