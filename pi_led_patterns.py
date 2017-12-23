import RPi.GPIO as GPIO
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', help='Number of seconds between on and off', default=1)
parser.add_argument('-p', help='Pin Number to turn on and off', default='all')
args = parser.parse_args()

GPIO.setmode(GPIO.BCM)

targetPins = []
if args.p == "all":
  targetPins.extend([4,17,27,22])
else:
  targetPins.append(int(args.p))

button_pin = 5


for pin in targetPins:
  GPIO.setup(int(pin), GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

GPIO.output(targetPins, False)
isOn = False
isPressed = GPIO.input(button_pin)
turnedOn = True
pattern = 1

try:
  while True:
    pattern = GPIO.input(button_pin)
    print("Pattern: " + str(pattern))
    if isOn == False:
      GPIO.output(targetPins, True)
      isOn = True
    else:
      GPIO.output(targetPins, False)
      isOn = False
    if pattern == 1:
      time.sleep(float(args.t))
    else:
      time.sleep(float(args.t / 10))
except KeyboardInterrupt:
  GPIO.output(targetPins, False)
  GPIO.cleanup()
  print("GPIO Connection Cleaned...")
