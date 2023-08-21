import os
from pathlib import Path

import pandas as pd

from config import excluded_participants

from metadata import Metadata
from meta_from_file import get_metadata_from_functionals_file


def set_column_values(df, obj):
    for key, value in vars(obj).items():
        df[key] = value
    return df


file_metadatas = get_metadata_from_functionals_file()

path = "/home/tim/work/nexa/nexa-opensmile-processing/files/out/verimind_egemaps_v2_lld"


slices = []

for file in os.listdir(path):
    print("processing file: ", file)

    if file.startswith("."):
        continue
    else:
        filename = Path(file).stem

    meta = Metadata(filename)
    meta.set_metadata()

    if meta.participant in excluded_participants:
        continue

    for fm in file_metadatas:
        if fm.statement == meta.statement and fm.participant == meta.participant:

            df = pd.read_csv(os.path.join(path, file))

            set_column_values(df, fm)

            slices.append(df)


df = pd.concat(slices)
df.to_csv("files/out/master.csv", index=False)







