import os 

def write_csv(data: list, name_df: str, path: str = 'downloads')-> None:
    try:
        os.makedirs(path, exist_ok=True)
        file_path = os.path.join(path, f'{name_df}.csv')

        with open(file_path, 'w', encoding='utf-8') as f:
            for row in data:
                # перебераем линию 
                line = ','.join(str(item) for item in row)
                f.write(line + '\n')# и переход на другую строку
        print(f"Файл успешно сохранён: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


def read_csv(path: str)-> list:
    data = []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                # удаляем проблемные символы и разделяем строк по .
                row = line.strip().split(',')
                data.append(row)
        return data
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []



# import csv

# # для записи файла csv
# def write_csv(data: list, name_df: str, path: str = 'downloads'):
#     try:
#         os.makedirs(path, exist_ok=True)
#         file_path = os.path.join(path, f'{name_df}.csv')

#         with open(file_path, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerows(data)
        
#         print(f"Файл успешно сохранён: {file_path}")

#     except Exception as e:
#         print(f"При записи произошла ошибка! {e}")    
            
# # для чтения файла csv
# def read_csv(path: str):
#     data = []
#     try:
#         with open(path, mode='r', encoding='utf-8') as file:
#             reader = csv.reader(file)
#             data = list(reader)       
#             return data 
#     except Exception as e:
#         print(f"При чтении произошла ошибка! {e}")


