import pytest

from src.reports.generate_report import generate_report

def test_generate_report():
    test_data = [['department', 'name', 'hours_worked', 'hourly_rate'], ['IT', 'Alice', '160', '50']]

    # тест report
    result = generate_report('report', [test_data])
    assert result[0] == ['', 'name', 'hours', 'rate']

    # тест на ValueError
    with pytest.raises(ValueError):
        generate_report('unknown', [test_data])
