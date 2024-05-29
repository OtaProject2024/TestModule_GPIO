import smbus

def scan_i2c():
    devices = []
    bus = smbus.SMBus(1)  # Raspberry Pi上のI2Cバス番号に応じて変更してください

    for address in range(0x03, 0x77):  # スキャンするI2Cアドレスの範囲を指定します
        try:
            bus.read_byte(address)
            devices.append(hex(address))
        except IOError:
            pass

    return devices

if __name__ == "__main__":
    print("Scanning I2C bus...")
    i2c_devices = scan_i2c()
    if i2c_devices:
        print("Detected devices:")
        for device in i2c_devices:
            print(device)
    else:
        print("No devices found.")
