import os
from pathlib import Path

from metadata import Metadata


def meta_from_dir():
    ret = []

    path = "/home/tim/work/nexa/nexa-opensmile-processing/files/out"
    for file in os.listdir(path):

        if file.startswith("."):
            continue
        else:
            filename = Path(file).stem

        meta = Metadata(filename)
        meta.set_metadata()

        ret.append(meta)

    return ret
