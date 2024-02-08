# Fingerprint project cli tool - Unlock your device using Biometrics

### Overview

This project involves creating a biometric security system that utilises an Arduino and a fingerprint scanner to unlock a PC or Mac. The system works by capturing and verifying fingerprints, allowing authorized users to access their computers.


https://github.com/MinasFakhori/fingerprint/assets/77994660/a94cf099-456f-4cae-8b5d-222d2cbd5e2f


--- 
### Requirements (Hardware)

* **Arduino Board** - As we are going to use the Keyboard library, you **must** have one of the following devices in [this list](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/). <br> To purchase the exact one I have, click [here](https://amzn.to/3SJWvPO).

* **Fingerprint Scanner Module** - purchase from [here](https://amzn.to/3HL91br).
* **Jumper Wires** - purchase from [here](https://amzn.to/49mP3zQ).
* **LED button** - purchase from [here](https://amzn.to/3SJ5Wz1).
* **PCB/Breadboard** - purchase from [here](https://amzn.to/3Ovm8kP).
* **Solder Iron** - purchase from [here](https://amzn.to/487qtSi).
* **Solder** - purchase from [here](https://amzn.to/4bpcJ8s).
* **Resistor** - purchase from [here](https://amzn.to/3uq4UOY).

---
### Software Requirements

* **Python** - You must have Python installed on your computer. You can download it from [here](https://www.python.org/downloads/).

* **Arduino CLI** - To be able to use the tools in this project, you must have the Arduino CLI installed. 

    For **Mac** users, you can install it by running the following command in your terminal:
    ```bash
    brew install arduino-cli
    ```
    Make sure you have Homebrew installed. If not, you can install it by running the following command in your terminal:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
    \
    For **Windows** and **Linux** users, you can install it from [here](https://arduino.github.io/arduino-cli/0.35/installation/).

* **Keyboard Library** - You can install the keyboard library by running the following command in your terminal:
    ```bash
    arduino-cli lib install "Keyboard"
    ```

* **Adafruit Fingerprint Sensor Library** - You can install the Adafruit Fingerprint Sensor Library by running the following command in your terminal:
    ```bash
    arduino-cli lib install "Adafruit Fingerprint Sensor Library"
    ```

---
### Project Setup Software

1. Download the project files
    ```bash
    git clone https://github.com/MinasFakhori/fingerprint
    ```
2. Navigate to the python project directory
    ```bash
    cd fingerprint/app
    ```

3. Make a virtual environment and activate it
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
4. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

---

### Usage

Note: You must have the Arduino connected to your computer and the fingerprint scanner connected to the Arduino. You can find the wiring diagram in the `diagrams` directory.

1. Go to the `app` directory
    ```bash
    cd fingerprint/app
    ```

2. Configure project
    ```bash
    python3.9 app.py project-config
    ```

3. Configure pinout (optional)
    If you don't know the pinout you can run the following command
    ```bash
    python3.9 app.py pinout-config ----show-pins
    ```
    If you wish to change the pinout run the following command
    ```bash
    python3.9 app.py pinout-config
    ```

4. Add a fingerprint
    You can add a fingerprint by running the following command:

    ```bash
    python3.9 app.py add-fingerprint
    ```

5. Activate the fingerprint scanner
    You can activate the fingerprint scanner by running the following command:
    ```bash
    python3.9 app.py activate-fingerprint
    ```


---

### Troubleshooting
If you encounter issues during setup or usage, consider the following:

Double-check hardware connections.
Make sure the Arduino supports the Keyboard library.
Review the wiring diagram for any errors.
Restart the Arduino and the computer.
If you are still experiencing issues, please open an issue on the project's GitHub page.
