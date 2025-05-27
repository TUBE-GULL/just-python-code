import pytest

from src.reports.bonus import bonus_calculation, add_bonus 


def test_bonus_calculation_above_threshold():
    assert bonus_calculation(160, 10) == 160 * 10 * 0.1

    
def test_bonus_calculation_below_threshold():
    assert bonus_calculation(140, 10) == 0

    
def test_bonus():
    test_data = [
        ['', 'name', 'hours', 'rate', 'payout'],
        ['Marketing', '', '', '', '', ''],
        ['', 'name1', '160', '50', '$8000'], # $8800
        ['Design', '', '', '', '', ''],
        ['', 'name2', '150', '40', '$6000'], # $6000
        ['', 'name3', '170', '60', '$10200'],# $11220
        ['HR', '', '', '', '', ''],
        ['', 'name4', '160', '45', '$7200'], # $6604
        ['', 'name5', '158', '38', '$6004'], # $6604
        ['Marketing', '', '', '', '', ''],
        ['', 'name6', '150', '35', '$5250'], # $5250
    ]
    
    
    result = add_bonus(test_data)
    
    # проверка заголовка
    assert 'bonus' in result[0]
    
    # получаю индекс поновой 
    bonus_idx = result[0].index('bonus')
    payout_idx = result[0].index('payout')
    
    #name1
    assert result[2][bonus_idx] == "$800.0"
    assert result[2][payout_idx] == "$8800"
    #name2
    assert result[4][bonus_idx] == "$0"
    assert result[4][payout_idx] == "$6000"
    #name3
    assert result[5][bonus_idx] == "$1020.0"
    assert result[5][payout_idx] == "$11220"
    #name4
    assert result[7][bonus_idx] == "$720.0"
    assert result[7][payout_idx] == "$7920"
    #name5
    assert result[8][bonus_idx] == "$600.4"
    assert result[8][payout_idx] == "$6604"
    #name6
    assert result[10][bonus_idx] == "$0"
    assert result[10][payout_idx] == "$5250"
    
    
def test_add_bonus_no_payout_column():
    test_data = [
        ['', 'name', 'hours', 'rate'],
        ['Marketing', '', '', '', ''],
        ['', 'name1', '160', '50', ], 
    ]

    with pytest.raises(ValueError, match="Нет колонки payout"):
        add_bonus(test_data)