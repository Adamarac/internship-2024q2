import json

from data.loadDataHandler import APISeriesIntervalDataLoader

if __name__ == '__main__':

    with open('parameters.json', 'r') as arquivo:
        parametros = json.load(arquivo)

    start_date = parametros['dates']['start_date']
    end_date =  parametros['dates']['end_date']

    serie_values_interval = APISeriesIntervalDataLoader(start_date,end_date)

    URLData = parametros['urlAPIParameters']
    BCBValues_df = serie_values_interval.requestSerieIntervalData(URLData)
    print(BCBValues_df)