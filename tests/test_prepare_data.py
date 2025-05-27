import pytest

from reports.prepare_data import search_hourly_rate, prepare_data

# тест для search_hourly_rate
def test_search_hourly_rate():
    headers_1 = ['id', 'name', 'department', 'hours_worked', 'hourly_rate']
    headers_2 = ['id', 'name', 'department', 'hours_worked', 'rate']
    headers_3 = ['id', 'name', 'department', 'hours_worked', 'salary']

    assert search_hourly_rate(headers_1) == 4
    assert search_hourly_rate(headers_2) == 4
    assert search_hourly_rate(headers_3) == 4

    # тест на отсутствие нужных колонок
    with pytest.raises(ValueError):
        search_hourly_rate(['id', 'name', 'department'])  # ValueError на headers.index

def test_prepare_data():
    test_data = [
        ['id', 'name', 'email', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'Alice', 'alice@example.com', 'Engineer', '160', '50'],
        ['2', 'Bob', 'bob@example.com', 'Manager', '170', '60'],
    ]

    expected = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice', 'Engineer', '160', '50'],
        ['2', 'bob@example.com', 'Bob', 'Manager', '170', '60'],
    ]

    result = prepare_data(test_data)
    assert result == expected

def test_prepare_data_with_rate():
    test_data = [
        ['id', 'name', 'email', 'department', 'hours_worked', 'rate'],
        ['1', 'Alice', 'alice@example.com', 'Engineer', '160', '55'],
    ]

    expected = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice', 'Engineer', '160', '55'],
    ]

    result = prepare_data(test_data)
    assert result == expected

def test_prepare_data_with_salary():
    test_data = [
        ['id', 'name', 'email', 'department', 'hours_worked', 'salary'],
        ['1', 'Alice', 'alice@example.com', 'Engineer', '160', '60'],
    ]

    expected = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', 'alice@example.com', 'Alice', 'Engineer', '160', '60'],
    ]

    result = prepare_data(test_data)
    assert result == expected
