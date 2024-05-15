import threading
import Led


def run(pin, wait):
    a = Led.Led(pin, wait)
    a.run()

if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(17, 2))
    t2 = threading.Thread(target=run, args=(18, 4))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
