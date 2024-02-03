from cli.utils import convert_range_arr


def arduino_pins(arduno_model: str) -> str:
    if arduno_model == "leonardo":
        return convert_range_arr(2, 19)
    elif arduno_model == "mega":
        return convert_range_arr(2, 69)
    elif arduno_model == "micro":
        return convert_range_arr(2, 16)
    elif arduno_model == "mini":
        return convert_range_arr(2, 13)
    elif arduno_model == "nano":
        return convert_range_arr(2, 19)
    elif arduno_model == "uno":
        return convert_range_arr(2, 19)
    else:
        return "Not supported"
