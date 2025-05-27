import argparse
# импорт функций 
from csv_tools import read_csv, write_csv
from reports.bonus import add_bonus
from reports.payout import add_payout
from reports.report import create_report, normalize_input
from reports.prepare_data import prepare_data


# для вызова 
def generate_report(report_type: str, data: list):
    reports = {
        'report': create_report,
        'payout': add_payout,
        'bonus': add_bonus 
        # сюда можно добавить новые отчёты
    }

    if report_type not in reports:
        raise ValueError(f"Отчёт '{report_type}' не поддерживается.")
    
    return reports[report_type](data)


def main():
    parser = argparse.ArgumentParser(description='Генерация отчётов по сотрудникам из CSV.')
    parser.add_argument('files', nargs='+', help='CSV-файлы с данными сотрудников')
    parser.add_argument('--report', required=True, help='Тип отчёта (например payout)')
    parser.add_argument('--save', action='store_true', help='Сохранять результат в файл')

    args = parser.parse_args()

    # если файлов будет больше в цикл 
    all_data = []
    for file in args.files:
        data = read_csv(file)
        prepared_data = prepare_data(data)
        all_data.append(prepared_data)
    
    normalized_data = normalize_input(*all_data)
    base_report = create_report(normalized_data) # сначала создаем базовый отчет
    
    if args.report == 'bonus':
        report_result = add_payout(base_report)  # добавляешь колонку payout и считаешь значения
        report_result = add_bonus(report_result) # потом добавляешь колонку bonus и считаешь значения
    elif args.report == 'payout':
        report_result = add_payout(base_report)
    else:
        report_result = generate_report(args.report, base_report)

    # Выводим результат
    for row in report_result:
        print(row)

    # записать В файл если --save
    if args.save:
        write_csv(report_result, args.report)


if __name__ == "__main__":
    main()
