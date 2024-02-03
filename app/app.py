import os

import typer

from cli.enroll import add_fingerprint_fun
from cli.fingerprint import unlock_device
from cli.password import write_dual_password, write_one_password
from cli.pin_config import get_current_pins, pin_menu
from cli.project_config import dual_devices_fun, serial_port, set_arduino
from cli.utils import get_arduino_device, get_config
from constant import PASSWORD_FILE

app = typer.Typer()


@app.command(name="project-config", help="Configure the project settings")
def project_config(
    set_port: bool = False, set_arduino_device: bool = False, dual_devices: bool = False
) -> None:
    if set_port:
        serial_port()
    elif set_arduino_device:
        set_arduino()
    elif dual_devices:
        dual_devices_fun()
    else:
        print("Configuring serial port")
        serial_port()
        print("Configuring Arduino device")
        set_arduino()
        print("Configuring dual devices")
        dual_devices_fun()


@app.command(
    name="pin-config",
    help="Configure the pin settings \nAdd --show-pins to get the current config",
)
def pin_config(show_pins: bool = False) -> None:
    if show_pins:
        current_pins = get_current_pins()
        for key, value in current_pins.items():
            print(f"{key}: {value}")
    else:
        device = get_arduino_device()
        pin_menu(device)


@app.command(name="add-fingerprint", help="Add a fingerprint")
def add_fingerprint() -> None:
    config = get_config()
    if config is None:
        print(
            "Please configure the project settings first by typing 'python app.py project-config'"
        )
        return
    else:
        add_fingerprint_fun()


@app.command(
    name="activate-fingerprint",
    help="Activate the fingerprint sensor. In activating it will ask for the password, this is the password that will be used to unlock the device. If dual devices is set to True, it will ask for two passwords.",
)
def activate_fingerprint() -> None:
    config = get_config()
    if config is None:
        print(
            "Please configure the project settings first by typing 'python app.py project-config'"
        )
        return

    dual_device = config["DUAL_DEVICES"].strip()
    arduino = config["ARDUINO"].strip()
    port = config["PORT"].strip()

    if dual_device == "False":
        write_one_password()
    else:
        write_dual_password()

    unlock_device(arduino, port)

    os.remove(PASSWORD_FILE)


if __name__ == "__main__":
    app()
