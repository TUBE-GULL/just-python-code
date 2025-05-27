# import pytest

# from unittest import mock
# import builtins
# import sys
# from reports import report

# def test_main_report(monkeypatch):
#     # подменим sys.argv
#     monkeypatch.setattr(sys, 'argv', [
#         'prog',
#         'file1.csv',
#         '--report', 'report'
#     ])

#     # подменим read_csv, prepare_data, write_csv
#     monkeypatch.setattr('reports.report.read_csv', lambda f: [['id', 'name', 'department', 'hours_worked', 'hourly_rate'], ['1', 'Alice', 'IT', '160', '50']])
#     monkeypatch.setattr('reports.report.prepare_data', lambda d: d)
#     monkeypatch.setattr('reports.report.write_csv', lambda data, name: None)

#     # подменим print чтобы ничего не выводилось
#     monkeypatch.setattr(builtins, 'print', lambda *args, **kwargs: None)

#     # вызвать main
#     report.main()

# def test_main_output(monkeypatch, capsys):
#     monkeypatch.setattr(sys, 'argv', [
#         'prog',
#         'file1.csv',
#         '--report', 'report'
#     ])
#     monkeypatch.setattr('reports.report.read_csv', lambda f: [['id', 'name', 'department', 'hours_worked', 'hourly_rate'], ['1', 'Alice', 'IT', '160', '50']])
#     monkeypatch.setattr('reports.report.prepare_data', lambda d: d)
#     monkeypatch.setattr('reports.report.write_csv', lambda data, name: None)

#     report.main()

#     captured = capsys.readouterr()
#     assert 'name' in captured.out  # проверяем что в выводе есть заголовок
