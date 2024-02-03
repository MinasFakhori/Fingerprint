import os

import serial.tools.list_ports


def get_serial_port():
    ports = serial.tools.list_ports.comports()
    cu_devices = [port.device for port in ports]

    print(
        "Please select one of the following ports that you are using for your Arduino:"
    )
    for i, device in enumerate(cu_devices, 1):
        print(f"{i}. {device}")

    while True:
        try:
            choice = int(input("Choose a device (enter the number): "))
            if 1 <= choice <= len(cu_devices):
                selected_device = cu_devices[choice - 1]
                print(f"You selected: {selected_device}")
                return f"{selected_device}\n"
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def arduino_types_fun():
    return [
        "leonardo",
        "mega",
        "micro",
        "mini",
        "nano",
        "uno",
    ]


def get_arduino_device():
    arduino_types = arduino_types_fun()

    print("Please select corresponds Arduino device:")

    for i, device in enumerate(arduino_types, 1):
        print(f"{i}. {device}")

    while True:
        try:
            choice = int(input("Choose a device (enter the number): "))
            if 1 <= choice <= len(arduino_types):
                selected_device = arduino_types[choice - 1]
                print(f"You selected: {selected_device}")
                selected_device = f"arduino:avr:{selected_device}\n"

                return selected_device
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def convert_txt_to_h(txt_file, h_file):
    with open(txt_file, "r") as txt:
        with open(h_file, "w") as h:
            for line in txt:
                l = line.split("=")
                line = f"#define {l[0]} {l[1]}"
                h.write(line)


def write_data_to_h_file(data, h_file):
    with open(h_file, "w") as h:
        for line in data:
            h.write(line)


def convert_range_arr(start, end):
    arr = []
    for i in range(start, end + 1):
        arr.append(i)
    return arr


def more_than_one_param(*args):
    if sum((args)) > 1:
        return True
    else:
        return False


def get_dual_device_ans():
    input_ans = input("Do you want to use dual devices (i.e., two passwords)? (Y/n): ")
    if (
        input_ans.lower() == "y"
        or input_ans.lower() == "yes"
        or input_ans.lower() == "yeah"
        or input_ans.lower() == "yup"
        or input_ans.lower() == "yep"
        or input_ans.lower() == "ya"
        or input_ans.lower() == "yea"
        or input_ans.lower() == ""
        or input_ans.lower() == " "
    ):
        return "True\n"
    else:
        return "False\n"


def get_config():
    if not os.path.exists("resources/config.txt"):
        with open("resources/config.txt", "w") as file:
            file.write("")
            return None
    with open("resources/config.txt", "r") as file:
        files = file.readlines()
        if len(files) == 0:
            return None
        config = {}
        for line in files:
            if line.strip():
                key, value = line.split("=")
                config[key] = value

    return config
