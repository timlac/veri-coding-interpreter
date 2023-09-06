import pandas as pd

from metadata.common_metadata import CommonMetadata


def get_metadata_from_records(file_path):
    metadata_columns = ["sttmnt_ID",
                        "Participant",
                        "Statement",
                        "Accuracy",
                        "Confidence_level",
                        "Confidence_type",
                        "Free_cued_recall"]

    df = pd.read_csv(file_path, delimiter=";")

    df = df[metadata_columns]

    # Rename a single column
    df.rename(columns={'sttmnt_ID': 'filename'}, inplace=True)

    # all column to lowercase
    df.rename(columns=lambda x: x.lower(), inplace=True)

    ret = []
    for _, row in df.iterrows():
        meta = CommonMetadata(**row)
        ret.append(meta)
    return ret
