import json

from data.loadDataHandler import APISeriesIntervalDataLoader
from data.dataFormatHandler import dataReshape
from data.saveDataHandler import saveCsv
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

    args = f'\n\nArgs\n\nstar_date: {start_date}\nend_date: {end_date}\ncapital: {capital}\nfrequency: {frequency}\n\n'

    print(args)
    print(dfCompound_reshaped)

    csv = parameters['general']['save_csv']
    boolean_value = csv.strip().upper() == "TRUE"

    if boolean_value:
        saveCsv(dfCompound_reshaped,"AmountEarnedData.csv")


    window = parameters['range']['days']
    amountEarned.calcBestEarn(window)
