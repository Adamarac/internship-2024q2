import pytest
import pandas as pd
from Calculator.amountEarnedHandler import calcAmountEarned 

@pytest.fixture
def example_df():
    data = {
        'data': ['01/01/2023', '01/02/2023', '01/03/2023', '01/04/2023'],
        'valor': [1.0, 2.0, 3.0, 4.0]
    }
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    return df

def test_valid_capital(example_df):
    calc = calcAmountEarned(1000.0, example_df)
    assert calc.capital == 1000.0

def test_invalid_capital(example_df):
    with pytest.raises(SystemExit):
        calc = calcAmountEarned("invalid_capital", example_df)

def test_calc_earned(example_df):
    calc = calcAmountEarned(1000.0, example_df)
    result_df = calc.CalcEarned()
    
    expected_data = {
        'data': pd.to_datetime(['01/01/2023', '01/02/2023', '01/03/2023', '01/04/2023'], format='%d/%m/%Y'),
        'valor': [1.0, 2.0, 3.0, 4.0],
        'Capital': [1000.0, 1000.0 * (1 + 1.0 / 100), 1000.0 * (1 + 2.0 / 100) * (1 + 1.0 / 100), 1000.0 * (1 + 3.0 / 100) * (1 + 2.0 / 100) * (1 + 1.0 / 100)],
        'Amount Earned': [0.0, 1000.0 * (1 + 1.0 / 100) - 1000.0, 1000.0 * (1 + 2.0 / 100) * (1 + 1.0 / 100) - 1000.0, 1000.0 * (1 + 3.0 / 100) * (1 + 2.0 / 100) * (1 + 1.0 / 100) - 1000.0]
    }
    expected_df = pd.DataFrame(expected_data)
    expected_df['data'] = pd.to_datetime(expected_df['data'], format='%d/%m/%Y')
    
    pd.testing.assert_frame_equal(result_df, expected_df)
