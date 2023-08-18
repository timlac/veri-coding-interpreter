import os
import pandas as pd
from pathlib import Path

from meta_from_file import get_metadata_from_functionals_file
from meta_from_dir import meta_from_dir

from metadata import Metadata


def find_non_matching_objects(metas1, metas2):
    ret = []

    for m1 in metas1:
        found = False

        for m2 in metas2:
            if m1.participant == m2.participant and m1.statement == m2.statement:
                found = True

        if not found:
            ret.append(m1)

    return ret


def list2df(input_list):
    return pd.DataFrame([vars(m) for m in input_list])


file_metadatas = get_metadata_from_functionals_file()

dir_metadatas = meta_from_dir()

dir_not_in_file = find_non_matching_objects(dir_metadatas, file_metadatas)
df_dir_not_in_file = list2df(dir_not_in_file)
df_dir_not_in_file.to_csv("files/out/missing/files_not_found_in_csv.csv")

file_not_in_dir = find_non_matching_objects(file_metadatas, dir_metadatas)
df_file_not_in_dir = list2df(file_not_in_dir)
df_file_not_in_dir.to_csv("files/out/missing/csv_rows_not_found_in_files.csv")
