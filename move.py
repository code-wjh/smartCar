import RPi.GPIO as GPIO
import time

AIN1 = 18
AIN2 = 19
PWMA = 13
BIN1 = 20
BIN2 = 21
PWMB = 12


def setup():
    global l_motor
    global r_motor
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    GPIO.setup(AIN1, GPIO.OUT)
    GPIO.setup(AIN2, GPIO.OUT)
    GPIO.setup(BIN1, GPIO.OUT)
    GPIO.setup(BIN2, GPIO.OUT)
    l_motor = GPIO.PWM(PWMA, 500)
    r_motor = GPIO.PWM(PWMB, 500)
    l_motor.start(0)
    r_motor.start(0)


def turn_up(speed, t):
    l_motor.ChangeDutyCycle(speed)
    r_motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 1)
    GPIO.output(BIN2, 1)
    time.sleep(t)


def turn_down(speed, t):
    l_motor.ChangeDutyCycle(speed)
    r_motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, 1)
    GPIO.output(BIN1, 1)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)
    time.sleep(t)


def turn_right(speed, t):
    l_motor.ChangeDutyCycle(speed)
    r_motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, 1)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 1)
    time.sleep(t)


def turn_left(speed, t):
    l_motor.ChangeDutyCycle(speed)
    r_motor.ChangeDutyCycle(speed)
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 1)
    GPIO.output(AIN2, 1)
    GPIO.output(BIN2, 0)
    time.sleep(t)


def stop(t):
    GPIO.output(AIN1, 0)
    GPIO.output(BIN1, 0)
    GPIO.output(AIN2, 0)
    GPIO.output(BIN2, 0)
    time.sleep(t)


def loop():
    while 1:
        turn_up(30, 0)


def destory():
    stop(0)
    GPIO.cleanup()
    l_motor.stop()
    r_motor.stop()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destory()