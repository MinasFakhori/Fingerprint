from cli.utils import (get_arduino_device, get_dual_device_ans,
                       get_serial_port, write_data_to_h_file)
from constant import PROJECT_CONFIG


def project_config_base(project_type: str, fun: function, isDual: bool) -> None:
    old = "no {project_type}"
    user_input = ""
    new = ""
    lines = []

    with open(PROJECT_CONFIG, "r") as config:
        lines_exist = False
        config_lines = config.readlines()
        for line in config_lines:
            if project_type.upper() in line:
                old = line.split("=")[1].strip()
                lines_exist = True
            else:
                lines.append(line)

    if not lines_exist:
        print(f"No {project_type} found in config file")
        new = fun()
        lines.append(f"{project_type.upper()}={new}")
        str_lines = "".join(lines)
        with open("resources/config.txt", "w") as config:
            config.write(f"{str_lines}")

    if old != "no {project_type}":
        print(f"Current {project_type}: {old}")
        user_input = input(f"Do you want to change the {project_type}? (Y/n): ")

        if (
            user_input.lower() == "n"
            or user_input.lower() == "no"
            or user_input.lower() == "nah"
        ):
            print(f"{project_type} not changed")
        else:

            new = fun()

            lines.append(f"{project_type.upper()}={new}")

            str_lines = "".join(lines)
            with open("resources/config.txt", "w") as config:
                config.write(f"{str_lines}")

            if isDual:
                new = new.strip()
                new = new.lower()
                write_data_to_h_file(
                    [f"#define {project_type.upper()} {new}"],
                    "../cpp/Fingerprint/dual_devices.h",
                )


def serial_port() -> None:
    project_config_base("port", get_serial_port, isDual=False)


def dual_devices_fun() -> None:
    project_config_base("dual_devices", get_dual_device_ans, isDual=True)


def set_arduino() -> None:
    project_config_base("arduino", get_arduino_device, isDual=False)
