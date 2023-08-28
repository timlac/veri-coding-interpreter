import math

import pandas as pd

from utils import remove_non_numeric


class MetaRecord:
    def __init__(self, sttmnt_id,
                 participant,
                 statement,
                 accuracy,
                 confidence_level,
                 confidence_type,
                 free_cued_recall):

        self.filename = str(sttmnt_id)
        self.participant = int(participant)

        self.statement = float(remove_non_numeric(statement))

        self.accuracy = int(accuracy)

        if not math.isnan(confidence_level):
            self.confidence_level = int(confidence_level)
        else:
            self.confidence_level = confidence_level

        if not math.isnan(confidence_type):
            self.confidence_type = int(confidence_type)
        else:
            self.confidence_type = confidence_type

        self.free_cued_recall = int(free_cued_recall)


def get_metadata_from_functionals_file():
    """
    Read records file and return a list of metadata objects
    :return:
    """

    path = "../files/functionals/audiovittne2_for_machlearn.csv"

    df_full = pd.read_csv(path, delimiter=";")
    df = df_full[["sttmnt_ID",
                  "Participant",
                  "Statement",
                  "Accuracy",
                  "Confidence_level",
                  "Confidence_type",
                  "Free_cued_recall"
                  ]]

    df["sttmnt_ID"] = df["sttmnt_ID"].str.replace(".wav", "")
    df["sttmnt_ID"] = df["sttmnt_ID"].str.replace("'", "")
    df["sttmnt_ID"] = df["sttmnt_ID"].str.replace('"', '')

    df.rename(columns=lambda x: x.lower(), inplace=True)

    record_list = []
    for index, row in df.iterrows():
        record = MetaRecord(**row)
        record_list.append(record)

    return record_list


if __name__ == "__main__":
    m = get_metadata_from_functionals_file()
