import subprocess
import time

import serial

from cli.utils import get_config


def add_fingerprint_fun():
    ARDUINO_SKETCH = "../cpp/Enroll/Enroll.ino"
    print("Adding Fingerprint")

    config = get_config()

    serial_port = config["PORT"].strip()
    arduino_device = config["ARDUINO"].strip()

    subprocess.run(["arduino-cli", "compile", "--fqbn", arduino_device, ARDUINO_SKETCH])

    subprocess.run(
        [
            "arduino-cli",
            "upload",
            "-p",
            serial_port,
            "--fqbn",
            arduino_device,
            ARDUINO_SKETCH,
        ]
    )
    try:
        read_data(serial_port)
    except Exception as e:
        print(
            f"Error:{e} \nRun the command 'python app.py project-config' to configure the project settings"
        )


def read_data(port):
    print("Reading serial output...")

    port = port.strip()

    finger_added = []

    not_finished = True

    with serial.Serial(port, 9600) as ser:
        time.sleep(2)
        while not_finished:
            line = ser.readline().decode("utf-8").strip()
            if line:
                if not "type" in line:
                    print(line)
                else:
                    print(
                        "Enter Fingerprint Number from 1 to 127. \ne or exit to quit: "
                    )
                    user_num = input()
                    if user_num.isnumeric() and int(user_num) > 127:
                        print("Fingerprint number should be between 1 and 127")
                        continue

                    if user_num.lower() == "exit" or user_num.lower() == "e":
                        if len(finger_added) == 0:
                            print("No Fingerprints Added")
                        elif len(finger_added) == 1:
                            print(
                                "Exiting...\nAdded Fingerprint number: ",
                                finger_added[0],
                            )
                        else:
                            print(
                                "Exiting...\nAdded Fingerprint numbers: ", finger_added
                            )
                        not_finished = False
                        break
                    finger_added.append(user_num)
                    ser.write(user_num.encode("utf-8"))
