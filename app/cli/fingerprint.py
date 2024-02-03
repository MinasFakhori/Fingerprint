import subprocess
import time

import serial

from cli.utils import get_serial_port


def unlock_device(arduino_device, serial_port):
    ARDUINO_SKETCH = "../cpp/Fingerprint/Fingerprint.ino"

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

    return True
