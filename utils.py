import re


def remove_non_numeric(input_string):
    if isinstance(input_string, str):
        # Keep only digits, commas, and hyphens
        input_string = re.sub(r'[^\d,-.]+', '', input_string)
        input_string = input_string.replace(',', '.')
        input_string = input_string.replace('-', '.')

    input_string = float(input_string)

    return input_string
