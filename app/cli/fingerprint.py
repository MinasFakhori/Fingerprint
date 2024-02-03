import subprocess
from constant import ACTIVATE



def unlock_device(arduino_device:str, serial_port:str)-> None:
    ARDUINO_SKETCH = ACTIVATE

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
