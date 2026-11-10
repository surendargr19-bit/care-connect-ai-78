# Button device: wiring and setup

## Parts
- Raspberry Pi Pico (about Rs 400)
- Big arcade push button (normally open)
- Micro-USB cable (data cable, not charge-only)
- OTG adapter for an Android phone (USB-A to USB-C or micro-USB)

## Wiring
```
Button leg 1  ->  GP15 (pin 20)
Button leg 2  ->  GND  (pin 18)
```
No resistor is needed. The code uses the Pico's internal pull-up.

## Software setup
1. Hold the **BOOTSEL** button on the Pico, plug it into your computer, and release. A drive called `RPI-RP2` appears.
2. Download the CircuitPython `.uf2` file for the Pico from circuitpython.org and drag it onto that drive. The Pico restarts as `CIRCUITPY`.
3. From the CircuitPython library bundle, copy the `adafruit_hid` folder into `CIRCUITPY/lib/`.
4. Copy `device/code.py` to the root of `CIRCUITPY` as `code.py`.

## Test
1. Open any text box on your computer and press the button. A space appears.
2. Plug the Pico into the phone through the OTG adapter.
3. Open the CareConnect app. Press the button to start scanning, press again to select, hold for 2 seconds for Emergency.

## Troubleshooting
- Nothing happens: use a data USB cable and check the button is on GP15 and GND.
- Phone does not react: check that the OTG adapter works with another USB device.
