from datetime import datetime, timedelta

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
    def CalcEarned(self) -> pd.DataFrame:

        _df = self.df.copy()
        _df["Capital"] = self.capital
        _df["Capital"] = (_df["Capital"]) * (_df["valor"]/100).shift().add(1).cumprod().fillna(1)
        logging.info("Compound have been calculated")

        _df['Amount Earned'] = _df["Capital"] - self.capital
        logging.info("Amount earned have been calculated")

        return _df      

    #Returns the last row of the DataFrame with the highest amount
    def calc_sum_range(self, start_date, end_date, df):
        _df = df[(df["data"] >= start_date) & (df["data"] <= end_date)].copy()
        _df.loc[:, "x"] = self.capital
        _df.loc[:, "x"] = _df["x"] * (_df["valor"]/100).shift().add(1).cumprod().fillna(1)
        val = _df.iloc[-1]["x"]

        return val
    
    #Calculates the best date to invest within a time window
    def calcBestEarn(self,range_of:int):
        df = self.df
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

        max_Date = df.iloc[-1]["data"] - timedelta(days=range_of)
        indice = df[df['data'] <= max_Date].index
        length = indice[-1] + 1

        best_start = None
        best_end = None
        best_value = 0

        logging.info("Search for window with the best profit initiated")
        #Iterates over each window and updates the variables if a better result is found
        for i in range(0, length):
            start = df.iloc[i]["data"]
            end_date = start + timedelta(days=range_of)
            end_index = df[df['data'] <= end_date].index

            if len(end_index) == 0:
                continue

            end_index_int = end_index[-1]
            end = df.iloc[end_index_int]["data"]
            value = self.calc_sum_range(start, end, df)
            
            if value > best_value:
                best_start = start
                best_end = end
                best_value = value

        logging.info("Best window found")
        print(
            f"\n\nThe best day to invest is {best_start.date()}, with an amount earned of {best_value} after {range_of} "
            f"days ({best_start.date()} to {best_end.date()}\n\n)"
        )



setup_logging()