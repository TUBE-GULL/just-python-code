from reports.bonus import add_bonus
from reports.payout import add_payout
from reports.report import create_report

# для вызова 
def generate_report(report_type: str, data: list):
    reports = {
        'report': create_report,
        'payout': add_payout,
        'bonus': add_bonus 
        # сюда можно добавить новые отчёты
    }

    if report_type not in reports:
        raise ValueError(f"Отчёт '{report_type}' не поддерживается. Доступные отчёты: {', '.join(reports.keys())}")
    
    return reports[report_type](data)
