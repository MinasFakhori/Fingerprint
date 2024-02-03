from getpass import getpass

from constant import PASSWORD_FILE


def write_one_password() -> None:
    input_password = getpass("Enter a password: ")
    with open(PASSWORD_FILE, "w") as file:
        file.write(f'#define PASSWORD1 "{input_password}"')
        file.write(f'\n#define PASSWORD2 "{input_password}"')
    print("Password set successfully")


def write_dual_password() -> None:
    input_password = getpass("Enter the first password: ")
    with open(PASSWORD_FILE, "w") as file:
        file.write(f'#define PASSWORD1 "{input_password}"')
    print("First password set successfully")

    input_password = getpass("Enter the second password: ")
    with open(PASSWORD_FILE, "a") as file:
        file.write(f'\n#define PASSWORD2 "{input_password}"')
    print("Second password set successfully")
