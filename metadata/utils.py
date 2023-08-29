import math
import re


def get_digits_only(input_string):
    """
    :param input_string: some string that may contain digits and characters
    :return: only digits
    """
    if isinstance(input_string, str):
        input_string = re.sub("\\D", "", input_string)

    # cast return value as int
    input_string = int(input_string)
    return input_string


def transform_to_float(input_string):
    if isinstance(input_string, str):
        # Keep only digits, commas, and hyphens
        input_string = re.sub(r'[^\d,-.]+', '', input_string)

        # replace comma (,) with dot (.)
        input_string = input_string.replace(',', '.')

        # replace dash (-) with dot (.)
        input_string = input_string.replace('-', '.')

    # cast return value as float
    input_string = float(input_string)

    return input_string


def handle_nan(val):
    """
    :param val: 0
    :return: if val is not nan, return val as int
            if nan return 0
    """
    if not math.isnan(val):
        return int(val)
    else:
        return val
