import json

from data.loadDataHandler import APISeriesIntervalDataLoader
from Calculator.amountEarnedHandler import calcAmountEarned

if __name__ == '__main__':

    with open('parameters.json', 'r') as arquivo:
        parameters = json.load(arquivo)

    start_date = parameters['dates']['start_date']
    end_date =  parameters['dates']['end_date']

    serie_values_interval = APISeriesIntervalDataLoader(start_date,end_date)

    URLData = parameters['urlAPIParameters']
    BCBValues_df = serie_values_interval.requestSerieIntervalData(URLData)

    capital = parameters['general']['capital']
    amountEarned = calcAmountEarned(capital,BCBValues_df)

    frequency = parameters['dates']['frequency']
    dfCompound = amountEarned.CalcEarned()

    window = parameters['range']['days']
    amountEarned.calcBestEarn()
