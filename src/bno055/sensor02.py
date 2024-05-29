import time
import smbus
import math
from gpiozero import Robot  # ロボット制御ライブラリ

# PID制御の定数
KP = 1.0
KI = 0.0
KD = 0.0

# 目標方向
TARGET_DIRECTION = 0

# PID制御器の初期化
class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def update(self, error):
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

# Raspberry Pi上のI2Cバス番号に応じて変更してください
i2c_bus_number = 1
sensor = smbus.SMBus(i2c_bus_number)

# ロボットの初期化
robot = Robot(left=(7, 8), right=(24, 23))  # 左右のモーターのGPIOピン番号に合わせて修正

# PID制御器の初期化
pid_controller = PIDController(KP, KI, KD)

try:
    while True:
        # BNO055から磁気センサーの値を取得
        magnetometer_x, magnetometer_y, magnetometer_z = sensor.magnetic

        # 磁気センサーの値から方向を計算
        direction = math.degrees(math.atan2(magnetometer_y, magnetometer_x))

        # 方向の誤差を計算
        error = TARGET_DIRECTION - direction

        # PID制御器に誤差を入力し、修正量を取得
        correction = pid_controller.update(error)

        # モーターの速度を計算
        left_speed = 0.5 + correction
        right_speed = 0.5 - correction

        # モーターを制御してロボットを動かす
        robot.left_motor.value = left_speed
        robot.right_motor.value = right_speed

        # 一定の間隔で処理を繰り返す（例：0.1秒ごとに処理を実行）
        time.sleep(0.1)

except KeyboardInterrupt:
    # Ctrl+Cが押された場合にプログラムを終了する
    robot.stop()
