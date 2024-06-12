import time
import RPi.GPIO as GPIO


class DCMotor:
    def __init__(self, pin1=20, pin1=21):
        self.pin1 = pin1
        self.pin2 = pin2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)


    def run(self, time=15):
        GPIO.output(self.pin1, GPIO.HIGH)
        GPIO.output(self.pin2, GPIO.LOW)
        time.sleep(time)

        GPIO.cleanup([self.pin1, self.pin2])


if __name__ == '__main__':
    a = DCMotor()
    a.run(30)
