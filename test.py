import RPi.GPIO as GPIO
import time
import board
import neopixel

in1 = 23
in2 = 24
in3 = 25
in4 = 12
ena = 18
enb = 26
temp1 = 1
trigger = 4
echo = 17
button = 27
lights = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(ena, 1000)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

pixel_pin = board.D18
num_pixels = 4

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

pixels.fill((255, 0, 0))
pixels.show()


def distance():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    startTime = time.time()
    StopTime = time.time()
    while GPIO.input(echo) == 0:
        startTime = time.time()
    while GPIO.input(echo) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - startTime
    dist = (TimeElapsed * 34300) / 2
    return dist


p.start(100)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while 1:
    if GPIO.input(button) == GPIO.LOW:
        print("hello")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        p.ChangeDutyCycle(100)
        print(distance())
        break

while 1:

    x = input()

    if x == 'r':
        print("run")
        if temp1 == 1:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            print("backward")
            x = 'z'

    elif x == 's':
        print("stop")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(75)
        x = 'z'

    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(100)
        x = 'z'

    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
