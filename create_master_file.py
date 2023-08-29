import os
from pathlib import Path

import pandas as pd

from constants import excluded_participants

from readers.read_records import get_metadata_from_records
from readers.read_files import filename2metadata


def set_column_values(df, obj):
    for key, value in vars(obj).items():
        df[key] = value
    return df


record_metadatas = get_metadata_from_records()

opensmile_files_directory = "/home/tim/Work/nexa/nexa-opensmile-processing/files/out"


slices = []

for file in os.listdir(opensmile_files_directory):
    print("processing file: ", file)

    if file.startswith(".gitkeep"):
        continue
    else:
        filename = Path(file).stem

    file_metadata = filename2metadata(filename)

    print(file_metadata.participant)
    print(type(file_metadata.participant))

    if file_metadata.participant in excluded_participants:
        print("file {} is in excluded participants, skipping...".format(filename))
        continue

    for record_metadata in record_metadatas:
        if record_metadata == file_metadata:

            df = pd.read_csv(os.path.join(opensmile_files_directory, file))

            set_column_values(df, record_metadata)

            slices.append(df)


df = pd.concat(slices)
df.to_csv("files/out/master_functionals.csv", index=False)







