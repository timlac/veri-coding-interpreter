import os
from pathlib import Path

import pandas as pd

from constants import excluded_participants

from read_records import get_metadata_from_records
from read_files import filename2metadata


def set_column_values(df, obj):
    for key, value in vars(obj).items():
        df[key] = value
    return df


record_metadatas = get_metadata_from_records()

path = "/home/tim/work/nexa/nexa-opensmile-processing/files/out/verimind_egemaps_v2_lld"


slices = []

for file in os.listdir(path):
    print("processing file: ", file)

    if file.startswith("."):
        continue
    else:
        filename = Path(file).stem

    file_metadata = filename2metadata(filename)

    if file_metadata.participant in excluded_participants:
        continue

    for record_metadata in record_metadatas:
        if record_metadata == file_metadata:

            df = pd.read_csv(os.path.join(path, file))

            set_column_values(df, record_metadata)

            slices.append(df)


df = pd.concat(slices)
df.to_csv("files/out/master.csv", index=False)







