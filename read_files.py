import os
from pathlib import Path
import re

from common_metadata import CommonMetadata


def filename2metadata(filename):
    name_list = filename.split("_")

    study = name_list[0]
    participant = name_list[1]
    session = name_list[2]
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

        meta = filename2metadata(filename)

        ret.append(meta)

    return ret
