import move
import RPi.GPIO as GPIO

sensor_left = 17
sensor_right = 16


def setup():
    GPIO.setup(sensor_left, GPIO.IN)
    GPIO.setup(sensor_right, GPIO.IN)


def loop():
    while 1:
        SR = GPIO.input(sensor_right)
        SL = GPIO.input(sensor_left)
        if SR == 1 and SL == 1:
            move.turn_up(50, 0)
        elif SR == 0 and SL == 1:
            move.turn_left(50, 0)
        elif SR == 1 and SL == 0:
            move.turn_right(50, 0)
        else:
            move.stop(1)
            move.turn_down(50, 0.5)
            move.turn_left(50, 0.5)


if __name__ == '__main__':
    move.setup()
    setup()
    try:
        loop()

    except KeyboardInterrupt:
        move.destory()