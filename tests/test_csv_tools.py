from src.csv_tools import write_csv, read_csv

def test_write_and_read_csv(tmp_path):
    # Тестовые данные
    test_data = [
        ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],
        ['1', '1@example.com', 'name1', 'lastname1', '999', '1'],
        ['2', '2@example.com', 'name2', 'lastname2', '888', '2'],
        ['3', '3@example.com', 'name3', 'lastname3', '777', '3'],
    ]
    test_filename = 'test_csv_write_read'
    
    
    # Путь к папке временных файлов
    path = tmp_path

    # Записываем файл
    write_csv(test_data, test_filename, str(path))

    # Путь к файлу
    file_path = path / f"{test_filename}.csv"
    assert file_path.exists()

    # Читаем файл
    result = read_csv(str(file_path))
    assert result == test_data # проверка на совпадения данных