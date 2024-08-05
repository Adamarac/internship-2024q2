import logging

import pandas as pd

from datetime import datetime


def setup_logging():
    log_filename = datetime.now().strftime('./loggs/%Y-%m-%d_%H-%M-%S')
    logging.basicConfig(
        level=logging.INFO,  
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),  
            logging.StreamHandler()  
        ]
    )


class dataReshape:

    def __init__(self,capital,frequency:str):
        self.capital = capital
        self.frequency = frequency
    
    def reshape_df(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Formating data")
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        df.set_index("data", inplace=True)
        if self.frequency == "D":
            df = df.groupby([df.index.date]).tail(1)
        elif self.frequency == "M":
            df = df.groupby([df.index.year, df.index.month]).tail(1)
        elif self.frequency == "Y":
            df = df.groupby([df.index.year]).tail(1)
        else:
            logging.error("Invalid frequency")
            exit()

        df = df.sort_index()
        df.drop(["valor"], axis="columns", inplace=True)
        df.index.names = ["Date"]
        logging.info("The data have been formated")

        return df

        


setup_logging()