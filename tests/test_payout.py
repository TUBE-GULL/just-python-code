import pytest

from src.reports.payout import rate_calculation, add_payout

def test_rate_calculation_valid():
    assert rate_calculation(160, 10) == "$1600"


def test_rate_calculation_invalid_input():
    assert rate_calculation("abc", 10) == ""
    assert rate_calculation(160, "xyz") == ""
    assert rate_calculation(None, 10) == ""
    assert rate_calculation(160, None) == ""


def test_add_payout_success():
    test_data = [
        ['','name','hours','rate'],
        ['Marketing','','','', ''],
        ['', 'name1', '160', '50'], 
        ['Design', '', '', '', ''],
        ['', 'name2', '150', '40'], 
        ['', 'name3', '170', '60'],
        ['HR', '', '', '', '', ''],
        ['', 'name4', '160', '45'], 
        ['', 'name5', '158', '38'], 
        ['Marketing','','','', ''],
        ['', 'name6', '150', '35'],  
    ]

    result = add_payout(test_data)
    
    assert 'payout' in result[0]
    payout_idx = result[0].index('payout')
    assert result[1][payout_idx] == ''
    assert result[2][payout_idx] == "$8000"
    assert result[3][payout_idx] == ''
    assert result[4][payout_idx] == "$6000"
    assert result[5][payout_idx] == "$10200"
    assert result[6][payout_idx] == ''
    assert result[7][payout_idx] == "$7200"
    assert result[8][payout_idx] == "$6004"
    assert result[9][payout_idx] == ''
    assert result[10][payout_idx] == "$5250"
    
def test_add_payout_missing_columns():
    data = [
        ['profession', 'hours'],
        ['Dev', '']
    ]

    with pytest.raises(ValueError):
        add_payout(data)