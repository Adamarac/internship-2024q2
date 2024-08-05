from io import StringIO
import requests
import pandas as pd
from datetime import datetime
import logging

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

#Class that handles data loading from the API
class APISeriesIntervalDataLoader:

    def __init__(self,start, end): 

        #Define start and end dates to the interval
        logging.info("Object instance created")
        self.start_date = start
        self.end_date = end
        logging.info(f'Defined datas {self.start_date} to start_date and {self.end_date} to end_date')

        #Validates the input dates
        self.isValid_dateInput()
        self.set_serie_id_map()
        logging.info("Defined series ID mapping")

    #Creates a dictionary with the series IDs
    def set_serie_id_map(self):
        self.sgs_code_mapping = {
            'SELIC': 11,
        }

    #Validates the input dates
    def isValid_dateInput(self):

        #Validate dates format
        try:
            self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
            self.end_date = datetime.strptime(self.end_date, '%Y-%m-%d')
        except ValueError as e:
            logging.error(f"Date format error: {e}")
            exit()

        #Validate if the start_date is greater than the minimum possible date
        min_date = datetime.strptime('1995-01-01','%Y-%m-%d')
        if self.start_date < min_date:
            logging.error("Invalid start date. Must be greater than or equal to 1995-01-01")
            exit()

        #Validates if the end date is after the start date
        if self.end_date < self.start_date:
            logging.error("Invalid end date. Must be later than start_date")
            exit()

        logging.info(f'The start and end dates have been validated (start:{self.start_date} end:{self.end_date})')

        #Converts the dates to the format used in the request URL
        self.start_date = self.start_date.strftime('%d/%m/%Y')
        self.end_date = self.end_date.strftime('%d/%m/%Y')

        logging.info(f'The start and end dates have been converted (start:{self.start_date} end:{self.end_date})')

    #Performs the request to the API
    def requestSerieIntervalData(self, parametersURL: dict) -> pd.DataFrame:

        self.URL = parametersURL
        url = self.URLStringBuilder()
        logging.info(f"Requesting URL: {url}")
        resp = requests.get(url)

        #Reads JSON and creates a DataFrame
        json_file = StringIO(resp.text)
        df = pd.read_json(json_file)
        
        return df
    
    #Builds the request string
    def URLStringBuilder(self) -> str:
        date_range_str = f"dataInicial={self.start_date}&dataFinal={self.end_date}"

        try:
            serie_id = self.sgs_code_mapping[self.URL["serie_name"]]
        except KeyError:
            serie_id = "Key not found"
            logging.error(serie_id)
            exit()

        logging.info(f'Founded key to {self.URL["serie_name"]}: {serie_id}')
        url_serie_id = f"bcdata.sgs.{serie_id}/"
        data_format = "dados?formato=json&"
        url = self.URL["baseURL"] + url_serie_id + data_format + date_range_str

        return url

setup_logging()