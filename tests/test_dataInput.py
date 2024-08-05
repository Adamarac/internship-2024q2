import pytest
from data.loadDataHandler import APISeriesIntervalDataLoader

def test_valid_dates():
    loader = APISeriesIntervalDataLoader('2023-01-01', '2023-12-31')
    assert loader.start_date == '01/01/2023'
    assert loader.end_date == '31/12/2023'

def test_invalid_date_format():
    with pytest.raises(SystemExit):
        loader = APISeriesIntervalDataLoader('01/01/2023', '2023-12-31')

def test_start_date_too_early():
    with pytest.raises(SystemExit):
        loader = APISeriesIntervalDataLoader('1994-12-31', '2023-12-31')

def test_end_date_before_start_date():
    with pytest.raises(SystemExit):
        loader = APISeriesIntervalDataLoader('2023-12-31', '2023-01-01')

def test_url_string_builder():
    loader = APISeriesIntervalDataLoader('2023-01-01', '2023-12-31')
    loader.URL = {
        'baseURL': 'https://api.bcb.gov.br/dados/serie/',
        'serie_name': 'SELIC'
    }
    url = loader.URLStringBuilder()
    expected_url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2023'
    assert url == expected_url

if __name__ == "__main__":
    pytest.main()
