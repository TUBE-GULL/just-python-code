import pytest

from reports.report import create_report

from reports import report
report.search_hourly_rate = lambda header: header.index('hourly_rate')

def test_create_report():
    data = [
        [  # первый файл (в реальной ситуации их может быть несколько)
            ['id', 'name', 'department', 'hours_worked', 'hourly_rate'],
            ['1', 'Alice', 'Engineer', '160', '50'],
            ['2', 'Bob', 'Engineer', '140', '50'],
            ['3', 'Charlie', 'Manager', '170', '60'],
        ]
    ]

    expected_result = [
        ['', 'name', 'hours', 'rate'],
        ['Engineer', '', '', '', ''],
        ['', 'Alice', '160', '50'],
        ['', 'Bob', '140', '50'],
        ['Manager', '', '', '', ''],
        ['', 'Charlie', '170', '60'],
    ]

    result = create_report(data)

    assert result == expected_result
