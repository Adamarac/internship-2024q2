from datetime import datetime

import logging
import pandas as pd

#Defines the logging behavior of the class
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

#Class that handles earn calculation
class calcAmountEarned:

    def __init__(self,capital:float,serie_interval_values: pd.DataFrame):
        logging.info("Object instance created")
        self.capital = capital

        #Validates the input capital
        self.isValid_capitalInput()

        self.df = serie_interval_values


    #Validates capital input data
    def isValid_capitalInput(self):
        try:
            self.capital = float(self.capital)
        except ValueError as e:
            logging.error(f'The capital value is not of a valid type: {self.capital}')
            exit()

        logging.info(f'The capital have been validated: {self.capital}')


    #Calculates the earn
    def CalcEarned(self,frequency:str) -> pd.DataFrame:

        _df = self.df
        _df["Capital"] = self.capital
        _df["Capital"] = (self.df["Capital"]) * (self.df["valor"]/100).shift().add(1).cumprod().fillna(1)
        logging.info("Compound have been calculated")

        _df['Amount Earned'] = _df["Capital"] - self.capital
        logging.info("Amount earned have been calculated")

        return _df
  
setup_logging()