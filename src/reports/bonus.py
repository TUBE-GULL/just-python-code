# типо бонус 10% если болье 150h 
def bonus_calculation(hours, rate):
    if int(hours) > 150:
        return (int(hours) * int(rate)) * 0.1
    else:
        return 0
    

def add_bonus(data):
    
    if 'payout' not in data[0]:
        raise ValueError("Нет колонки payout")
    else:
        payout_idx = data[0].index('payout')
    
    rate_inx = data[0].index('rate')
    hours_idx = data[0].index('hours')
    
    # новой колонки payout
    data[0].append('bonus')
    
    for row in data[1:]:
        if row and row[0] == '': # не типо профессии
            try:
                bonus = bonus_calculation(row[hours_idx], row[rate_inx]) 
            except Exception as e:
                  bonus = ''
            row.append(f"${bonus}")
            
            # делаю надбавку в зп ! 
            summa_pay = int(row[payout_idx].replace('$', ''))
            bonus_val = int(bonus)
            summa_pay += bonus_val   
            row[payout_idx] = f"${summa_pay}"
            
        else: # там где тип профессии
            row.append('')
            
    return data