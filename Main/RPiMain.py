#This file should run a DrumLooper out of the pygame GUI and from a raspberry pi. It doesn't work. and i broke the pi

import RPi.GPIO as GPIO
import time


Button = 11 ### SERIAL input
LATCH = 12 # #Clock pin/latch pin - RCLCK
SRCLK = 13 # shift register clock pin - SCLCK

def print_msg():
    print 'Program is running...'
    print 'Please press Ctrl+C to end the program...'


def setup():
    GPIO.setmode(GPIO.BOARD)  # Number GPIOs by its physical location
    GPIO.setup(Button, GPIO.IN)
    #GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)




def loop():
    ButtonState = [0] *8

    GPIO.output(SRCLK,GPIO.HIGH)
    GPIO.output(SRCLK, GPIO.LOW)
    for i in range(len(ButtonState)):
        GPIO.output(LATCH, GPIO.HIGH)
        GPIO.output(LATCH, GPIO.LOW)
        ButtonState[i] = GPIO.input(Button)

    print ButtonState
    time.sleep(2)
    #print "serial input: ", GPIO.input(Button)




def destroy():  # When program ending, the function is executed.
    GPIO.cleanup()


if __name__ == '__main__':  # Program starting from here
    #print_msg()
    setup()
    for i in xrange(500000):
     #   loop()
        print GPIO.input(12)
    GPIO.cleanup()
