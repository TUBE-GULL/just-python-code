# логика для рассчета зп думаю сюда можно и бонусы приктутиь и штрафы 
def rate_calculation(hours, rate):
    try:
        payout_value = int(hours) * int(rate)
        return f"${payout_value}"
    except (ValueError, TypeError):
        return ""  

def add_payout(data:list)->list:
    rate_inx = data[0].index('rate')
    hours_idx = data[0].index('hours')
    
    # новой колонки payout
    data[0].append('payout')
    
    for row in data[1:]:
        if row and row[0] == '': # не типо профессии
            try:
                payout = rate_calculation(row[hours_idx], row[rate_inx]) 
            except Exception as e:
                  payout = ''
            row.append(payout)
        else: # там где тип профессии
            row.append('')
        
    return data