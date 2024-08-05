import json

from data.loadDataHandler import APISeriesIntervalDataLoader
from data.dataFormatHandler import dataReshape
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

    frequency = parameters['dates']['frequency']
    reshape = dataReshape(capital,frequency)
    dfCompound_reshaped = reshape.reshape_df(dfCompound)

    print(dfCompound_reshaped)

    window = parameters['range']['days']
    amountEarned.calcBestEarn(window)
