import os
from pathlib import Path
import pandas as pd

from constants import wav_files_path, records_file_path, excluded_participants
from readers.read_records import get_metadata_from_records
from readers.read_files import filename2metadata

record_metadatas = get_metadata_from_records(records_file_path)

data = []

for directory in os.listdir(wav_files_path):

    dir_path = os.path.join(wav_files_path, directory)
    participant_dir = os.listdir(dir_path)

    for file in participant_dir:
        if file.endswith(".wav"):
            print("processing file: ", file)

            filename = Path(file).stem

            file_metadata = filename2metadata(filename)

            if file_metadata.participant in excluded_participants:
                print("file {} is in excluded participants, skipping...".format(filename))
                continue

            for record_metadata in record_metadatas:
                if record_metadata == file_metadata:

                    file_path = os.path.join(dir_path, file)

                    data_dict = {
                        "path": file_path,
                        "filename": record_metadata.filename,
                        "participant": record_metadata.participant,
                        "statement": record_metadata.statement,
                        "confidence_level": record_metadata.confidence_level,
                        "confidence_type": record_metadata.confidence_type,
                        "accuracy": record_metadata.accuracy,
                        "free_cued_recall": record_metadata.free_cued_recall
                    }

                    data.append(data_dict)


df = pd.DataFrame.from_records(data)
df.to_csv("files/out/master_file_mappings.csv", index=False)
