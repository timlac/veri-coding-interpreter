import re


def remove_non_numeric(input_string):
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
