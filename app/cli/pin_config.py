from os import path
from pathlib import Path

from cli.arduino_info import arduino_pins
from cli.utils import convert_txt_to_h

text_file = Path("resources/pinout.txt")

device = ""


def get_current_pins():
    current_pins = {}
    with open(text_file) as file:
        pinout = file.readlines()
        for line in pinout:
            if line == "\n":
                continue
            key = line.split("=")[0]
            value = line.split("=")[1].replace("\n", "").replace(" ", "")
            current_pins[key] = value
    return current_pins


def search_pin(pin_name):
    pin_name = pin_name.upper()
    if '"' in pin_name or "'" in pin_name:
        pin_name = pin_name.replace('"', "").replace("'", "")
    current_pins = get_current_pins()
    for key, value in current_pins.items():
        if key == pin_name:
            return value
    return None


def change_pins(pin_name, pin_value):
    pin_name = pin_name.upper()
    pin_value = int(pin_value)

    with open(text_file, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            old_pin_name = lines[i].split("=")[0]
            if pin_name == old_pin_name:
                new_line = f"{pin_name}={pin_value}\n"
                lines[i] = new_line

    with open(text_file, "w") as file:
        file.writelines(lines)


def pin_menu(device):

    device = device.split(":")[2].strip()

    available_pins = arduino_pins(device)

    current_pins = get_current_pins()

    for key, value in current_pins.items():
        title = f"'{key}'"
        new_value = input(
            f"Please enter a new value for {title} select from {available_pins[0]} to {available_pins[-1]}. Press enter for default pin:\n"
        )

        if new_value == "":
            new_value = value

        try:
            new_value = int(new_value)
        except ValueError:
            print(f"Using default value, pin {value}")

        if new_value not in available_pins:
            print(f"Pin {new_value} is not available. Using default pin {value}")

        pin_validation(title, new_value)


def pin_validation(pin_name, pin_value):

    old_pin = {}

    with open(text_file) as file:
        pinout = file.readlines()
        for line in pinout:
            title = line.split("=")[0]
            value = int(line.split("=")[1].replace("\n", "").replace(" ", ""))
            old_pin[value] = title

    if "'" or '"' in pin_name:
        pin_name = pin_name.replace("'", "").replace('"', "")

    if pin_value in old_pin.keys():

        if pin_name != old_pin[pin_value]:
            print(f"Pin {pin_value} is already used by {old_pin[pin_value]}.")
            switching_pin = search_pin(pin_name)
            user_in = input(
                f"Press [Y, n] to switch pin {pin_value} to {pin_name} and {old_pin[pin_value]} to pin {switching_pin}:\n"
            )
            if (
                user_in == ""
                or user_in == "Y"
                or user_in == "y"
                or user_in == "yes"
                or user_in == "Yes"
                or user_in == "YES"
                or user_in == "ye"
                or user_in == "Ye"
                or user_in == "YE"
            ):

                change_pins(pin_name, pin_value)
                change_pins(old_pin[pin_value], switching_pin)
    else:
        change_pins(pin_name, pin_value)

    convert_txt_to_h("resources/pinout.txt", "../cpp/Fingerprint/config.h")
    convert_txt_to_h("resources/pinout.txt", "../cpp/Enroll/config.h")
