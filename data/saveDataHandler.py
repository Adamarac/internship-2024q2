import glob
import pandas as pd

class saveCsv:

    def __init__(self, df, file_name):
            files_present = glob.glob(file_name)
            if not files_present:
                df.to_csv(file_name)
            else:
                print("File already exists, ignoring")