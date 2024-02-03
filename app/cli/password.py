from getpass import getpass


def write_one_password():
    is_success = False
    input_password = getpass("Enter a password: ")
    with open("../cpp/Fingerprint/password.h", "w") as file:
        file.write(f'#define PASSWORD1 "{input_password}"')
        file.write(f'\n#define PASSWORD2 "{input_password}"')
        is_success = True
    print("Password set successfully")
    return is_success


def write_dual_password():
    is_success = False
    input_password = getpass("Enter the first password: ")
    with open("../cpp/Fingerprint/password.h", "w") as file:
        file.write(f'#define PASSWORD1 "{input_password}"')
    print("First password set successfully")

    input_password = getpass("Enter the second password: ")
    with open("../cpp/Fingerprint/password.h", "a") as file:
        file.write(f'\n#define PASSWORD2 "{input_password}"')
        is_success = True
    print("Second password set successfully")

    return is_success
