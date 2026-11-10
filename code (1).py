# CareConnect AI - one-button USB device
# Board: Raspberry Pi Pico (CircuitPython) + adafruit_hid library in /lib
# Wiring: one leg of the button -> GP15, the other leg -> GND
#
# The Pico shows up as a USB keyboard. Each press sends the SPACE key.
# The web app (web/index.html) reads SPACE as the "select" button:
#   - short press while the screen is cycling = send that request
#   - hold for 2 seconds = send an Emergency request

import time

import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button = digitalio.DigitalInOut(board.GP15)
button.switch_to_input(pull=digitalio.Pull.UP)  # pressed = False (connected to GND)

keyboard = Keyboard(usb_hid.devices)

while True:
    if not button.value:                 # button pressed
        keyboard.press(Keycode.SPACE)    # key down
        while not button.value:          # keep it down while the button is held
            time.sleep(0.01)
        keyboard.release_all()           # key up
        time.sleep(0.05)                 # small debounce delay
    time.sleep(0.01)
