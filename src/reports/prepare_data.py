# пока будет тут так как она нужна для описка rate он может быть разынй 
def search_hourly_rate(headers:list):
    return  headers.index('hourly_rate') if 'hourly_rate' in headers else (
                 headers.index('rate') if 'rate' in headers else headers.index('salary'))
    

# данную функцию сделал если нужно просто отсортировать под один формат (если пользоваться panda то пофиг) а если повторно то может ии пригодиться 
def prepare_data(data:list):
    headers = data[0]
    index_id = headers.index('id')
    index_name = headers.index('name')
    index_email = headers.index('email')
    index_department = headers.index('department')
    index_hours_worked = headers.index('hours_worked')
    index_hourly_rate = search_hourly_rate(headers)
    
    # заменил на функцию 
    # if 'hourly_rate' in headers:
    #     index_hourly_rate = headers.index('hourly_rate')
    # elif 'rate' in headers:
    #     index_hourly_rate = headers.index('rate')
    # elif 'salary' in headers:
    #     index_hourly_rate = headers.index('salary')
    # else:
    #     index_hourly_rate = None
    #     print("Не найден столбец с тарифом/ставкой")
    
    
    # Заголовки, которые будем возвращать:
    new_data = [['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate'],]
    
    for i in data[1:]: 
        if index_hourly_rate is not None:
            
            t =[i[index_id],
                 i[index_email],
                 i[index_name],
                 i[index_department],
                 i[index_hours_worked],
                 i[index_hourly_rate]]
        
        # если нету данных по ставке 
        else:
            t =[i[index_id],
                i[index_email],
                i[index_name],
                i[index_department],
                i[index_hours_worked],
                i[0]]
        new_data.append(t)
    
    return new_data
