import time
import RPi.GPIO as GPIO

class Led:
    def __init__(self, pin=18, wait=3):
        self.pin = pin
        self.wait = wait

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)

    def run():
        print(f'pin:{self.pin} start')
        for i in range(5):
            GPIO.output(pin, True)
            time.sleep(wait)
            GPIO.output(pin, False)
            time.sleep(2)

        GPIO.cleanup(pin)
        print(f'pin:{self.pin} finish')
