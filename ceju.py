import time
import move
import RPi.GPIO as GPIO

trig = 27
echo = 26


def setup():
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)


def distance():
    GPIO.output(trig, 0)
    time.sleep(0.000002)
    GPIO.output(trig, 1)
    time.sleep(0.00001)
    GPIO.output(trig, 0)
    while GPIO.input(echo) == 0:
        pass
    t1 = time.time()
    while GPIO.input(echo) == 1:
        pass
    t2 = time.time()
    dur = t2 - t1
    print(dur * 340 / 2 * 100)
    return dur * 340 / 2 * 100


def loop():
    while 1:
        dist = distance()
        if dist < 60:
            move.turn_down(50, 1)
            move.turn_left(50, 1)
        else:
            move.turn_up(50, 1)


if __name__ == '__main__':
    try:
        move.setup()
        setup()
        loop()
    except KeyboardInterrupt:
        move.destory()