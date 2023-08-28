import pandas as pd

from read_records import get_metadata_from_records
from read_files import get_metadata_from_files


def find_non_matching_objects(metas1, metas2):
    ret = []

    for m1 in metas1:
        found = False

        for m2 in metas2:
            if m1 == m2:
                found = True

        if not found:
            ret.append(m1)

    return ret


def list2df(input_list):
    return pd.DataFrame([vars(m) for m in input_list])


record_metadatas = get_metadata_from_records()
file_metadatas = get_metadata_from_files()

files_not_in_records = find_non_matching_objects(file_metadatas, record_metadatas)
df_files_not_in_records = list2df(files_not_in_records)
df_files_not_in_records.to_csv("files/out/missing/files_not_found_in_csv.csv")

records_not_in_files = find_non_matching_objects(record_metadatas, file_metadatas)
df_records_not_in_files = list2df(records_not_in_files)
df_records_not_in_files.to_csv("files/out/missing/csv_rows_not_found_in_files.csv")
