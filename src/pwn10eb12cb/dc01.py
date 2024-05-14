import RPi.GPIO as GPIO
import time

class DcMotor:
    def __init__(self, in1=20, in2=21):
        self.in1 = in1
        self.in2 = in2
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)

    def mode_view(self):
        modes_operation = {
            (0, 0): 'ストップ(TSD, ISD解除)',
            (0, 1): '正転(正転)',
            (1, 0): '逆転(逆転)',
            (1, 1): 'ブレーキ(ブレーキ)'
        }
        print(f'モード：{modes_operation[mode]}, 入力(IN1, IN2)：({self.in1}, {self.in2}->{"H" if self.in1 else "L"}, {"H" if self.in2 else "L"})')

    def run(self):
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.LOW)
        print('初期条件')
        print_mode((GPIO.input(20), GPIO.input(21)))
        time.sleep(1) #1秒待つ
        print(f'{"#"*20}\n')

        try:
            while True:
                # 正転モード
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(21, GPIO.LOW)
                print_mode((GPIO.input(20), GPIO.input(21)))
                time.sleep(3
                # ストップモード
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.LOW)
                print_mode((GPIO.input(20), GPIO.input(21)))
                time.sleep(1
                # 逆転モード
                GPIO.output(20, GPIO.LOW)
                GPIO.output(21, GPIO.HIGH)
                print_mode((GPIO.input(20), GPIO.input(21)))
                time.sleep(3
                # ブレーキモード
                GPIO.output(20, GPIO.HIGH)
                GPIO.output(21, GPIO.HIGH)
                print_mode((GPIO.input(20), GPIO.input(21)))
                time.sleep(2)
        except KeyboardInterrupt:
            pass

        GPIO.cleanup()
