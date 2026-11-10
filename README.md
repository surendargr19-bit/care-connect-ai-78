# CareConnect AI

**One button for patients who cannot speak, type or call a nurse.**

Built for the Homingo Hackathon (Edition 01), Agents track.

## The problem

Patients in hospital beds or home care are often too weak, in pain, elderly or unable to speak clearly. Reaching a nurse for something simple like water, food or medicine can be hard, and in an emergency every second matters.

## Our solution

CareConnect AI lets a patient ask for help with **a single button**:

1. The patient presses the button (or taps the screen) and the app starts scanning.
2. Every **5 seconds** the screen automatically shows the next picture and question: Water, Food, Medicine, Emergency, Other.
3. When the patient sees what they need, they press the button once. The request goes straight to the nurse or medical staff.
4. **Hold the button for 2 seconds** to send an Emergency request immediately.
5. The nurse sees the request on a live dashboard, taps **Accept**, and the patient's screen shows "The nurse is coming".

The same button also works as a USB device that plugs into a phone like a mouse, so patients do not need to touch the screen.

## Features

- One-button "switch scanning" interface with large pictures
- Languages: English, Tamil and Tanglish
- Voice input (Web Speech API) as an extra way to ask
- AI priority: Emergency first, then Medicine, then Water and Food
- Repeat detection: if a patient asks for the same thing several times in 30 minutes, the nurse gets a note
- Smart hint: Food is highlighted at mealtimes
- Nurse dashboard with Accept, Done, request count and an alarm sound for emergencies
- Live sync between the patient phone and the nurse phone
- Large text and buttons, built for accessibility

## How it works

```
Patient button (USB)  ->  Patient screen (scans options every 5 s)
                                  |
                             request sent
                                  v
                      Shared database (live)
                                  |
                                  v
                Nurse dashboard: priority list, Accept, Done
                                  |
                  status goes back to the patient screen
```

## Repository structure

```
careconnect-ai/
  README.md
  LICENSE
  web/index.html      The app: patient screen and nurse dashboard in one file
  device/code.py      Raspberry Pi Pico firmware for the one-button USB device
  docs/wiring.md      Wiring and setup for the device
```

## Run the app

1. Open `web/index.html` in a browser (Chrome recommended).
2. **Patient view:** the default page. Press the big button or press the **Space** key.
3. **Nurse view:** open the same page with `#nurse` at the end of the address, for example `index.html#nurse`.
4. Open both in two tabs on the same device. A request from the patient tab appears on the nurse tab.

Note: this version shares data between tabs on one device. Syncing between different phones needs the cloud database, see the roadmap.

## Build the button device

See [docs/wiring.md](docs/wiring.md). In short: a Raspberry Pi Pico, a big push button, and a USB cable. The Pico acts as a USB keyboard that sends the Space key, so the phone needs no driver.

## Tech stack

- HTML, CSS and JavaScript (no framework)
- Web Speech API for voice input
- Raspberry Pi Pico with CircuitPython and `adafruit_hid` for the device

## Roadmap

- [ ] Firebase (Firestore) for real-time sync across phones
- [ ] Firebase Cloud Messaging or SMS alerts for the home nurse
- [ ] LLM agent to understand free speech and write a short summary for the nurse
- [ ] 3D-printed case for the button device
- [ ] Android app version (Kotlin, Jetpack Compose)

## Team

- [Your name], BE Computer Science and Engineering (Cyber Security)

## License

MIT, see [LICENSE](LICENSE).
