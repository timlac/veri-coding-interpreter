import os
from pathlib import Path
import re

from common_metadata import CommonMetadata


def get_digits_only(mixed_string):
    """
    :param mixed_string: some string that may contain digits and characters
    :return: only digits
    """
    ret = re.sub("\\D", "", mixed_string)
    return int(ret)


def process_filename(filename):
    name_list = filename.split("_")

    study = get_digits_only(name_list[0])
    participant = get_digits_only(name_list[1])
    session = get_digits_only(name_list[2])
    statement = name_list[3]

    meta = CommonMetadata(filename=filename,
                          study=study,
                          participant=participant,
                          session=session,
                          statement=statement)

    return meta


def get_metadata_from_files():
    ret = []

    path = "/home/tim/Work/nexa/nexa-opensmile-processing/files/out"
    for file in os.listdir(path):

        if file.startswith(".gitkeep"):
            continue
        else:
            filename = Path(file).stem

        meta = process_filename(filename)

        ret.append(meta)

    return ret