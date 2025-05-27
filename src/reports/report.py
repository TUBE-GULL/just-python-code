from reports.prepare_data import search_hourly_rate


# для получения одного или несколькиих файлов 
# если это один файл — оборачиваем его в список
def normalize_input(*data):
    
    result = []
    for i in data:
        # проверка если в list есть еще файл и он страка и первый элемент id !  
        if isinstance(i[0][0], str) and 'id' in i[0]:
            result.append(i)
        else:
            # если это уже список файлов — добавляем их
            result.append(i)
            
    return result


# данная функция нужна для того что бы уже подготовить результат рл зп 
def create_report(data:list):
    result  = [['', 'name', 'hours', 'rate']]
    # знаю что уже известно но думаю если подадут другой сет ! 
    department_idx = data[0][0].index('department')
    name_idx = data[0][0].index('name')
    hours_idx = data[0][0].index('hours_worked')
    rate_idx = search_hourly_rate(data[0][0])
        
    for file_data in data:
        group_data = {}
        
        # обьеденить в группы по профессиям 
        # поиск по профессиям 
        for i in file_data[1:]:
            dept = i[department_idx] # достаю названия профессии 
            group_data.setdefault(dept,[]).append(i) # фозращает [] еслии нет значения 


        # имя часы ставка result   
        for dept, rows in group_data.items():
            result.append([dept,'','','',''])

            # тут можно добавлять столбец и функцию
            for row in rows:
                result.append(['',
                               row[name_idx],
                               row[hours_idx],
                               row[rate_idx],
                               ])
            
    return result