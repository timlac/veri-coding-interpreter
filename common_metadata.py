import math
import re


def transform_to_float(input_string):
    if isinstance(input_string, str):
        # Keep only digits, commas, and hyphens
        input_string = re.sub(r'[^\d,-.]+', '', input_string)

        # replace comma (,) with dot (.)
        input_string = input_string.replace(',', '.')

        # replace dash (-) with dot (.)
        input_string = input_string.replace('-', '.')

    # cast return value as float
    input_string = float(input_string)

    return input_string


def handle_nan(val):
    """
    :param val: 0
    :return: if val is not nan, return val as int
            if nan return 0
    """
    if not math.isnan(val):
        return int(val)
    else:
        return val


class CommonMetadata:

    DEFAULT_FILENAME = None

    # all observations come from study 2
    DEFAULT_STUDY = 1000

    # somewhere between 1 and 100
    DEFAULT_STATEMENT = 1000

    # typically 2
    DEFAULT_SESSION = 1000

    # participant making the statements, somewhere between 1 and 100
    DEFAULT_PARTICIPANT = 1000

    # 1 = accurate
    # 0 = inaccurate
    DEFAULT_ACCURACY = 1000

    # somewhere between 0 and 100
    # NA when nothing
    # NA will default to nan, and we will leave it like that
    DEFAULT_CONFIDENCE_LEVEL = 1000

    # 1 = First time item is mentioned
    # 2 = Second, third etc. time item is mentioned
    # NA when nothing
    # Na will default to nan, and we will leave it like that
    DEFAULT_CONFIDENCE_TYPE = 1000

    # 1 = free recall
    # 2 = cued recall
    DEFAULT_FREE_CUED_RECALL = 1000

    def __init__(self,
                 filename=DEFAULT_FILENAME,
                 study=DEFAULT_STUDY,
                 statement=DEFAULT_STATEMENT,
                 session=DEFAULT_SESSION,
                 participant=DEFAULT_PARTICIPANT,
                 accuracy=DEFAULT_ACCURACY,
                 confidence_level=DEFAULT_CONFIDENCE_LEVEL,
                 confidence_type=DEFAULT_CONFIDENCE_TYPE,
                 free_cued_recall=DEFAULT_FREE_CUED_RECALL):

        self.filename = str(filename)
        self.study = int(study)
        self.statement = transform_to_float(statement)
        self.session = int(session)
        self.participant = int(participant)
        self.accuracy = int(accuracy)
        self.confidence_level = handle_nan(confidence_level)
        self.confidence_type = handle_nan(confidence_type)
        self.free_cued_recall = int(free_cued_recall)
