import re

from utils import remove_non_numeric


def get_digits_only(mixed_string):
    """
    :param mixed_string: some string that may contain digits and characters
    :return: only digits
    """
    ret = re.sub("\\D", "", mixed_string)
    return int(ret)


class Metadata:

    DEFAULT_STUDY = 100
    DEFAULT_STATEMENT = 100
    DEFAULT_SESSION = 100
    DEFAULT_PARTICIPANT = 100

    def __init__(self, filename):
        self.filename = filename

        self.name_list = filename.split("_")

        self.study = self.DEFAULT_STUDY
        self.statement = self.DEFAULT_STATEMENT
        self.session = self.DEFAULT_SESSION
        self.participant = self.DEFAULT_PARTICIPANT

    def set_metadata(self):
        self.study = get_digits_only(self.name_list[0])
        self.participant = get_digits_only(self.name_list[1])
        self.session = get_digits_only(self.name_list[2])
        self.statement = remove_non_numeric(self.name_list[3])



