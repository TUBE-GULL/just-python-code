from typing import Dict
import asyncio
import gdown
import os

file_links = {
    "data1": os.getenv("DATA1"),
    "data2": os.getenv("DATA2"),
    "data3": os.getenv("DATA3"),
}

def download_file(file_list: Dict[str, str],
                  dir: str ="..test_task/downloads")->bool:
    # создает папку 
    os.makedirs(dir, exist_ok=True)
    
    try:
        for name, url in file_list.items():
            dir = os.path.join(dir, f"{name}.csv")
            gdown.download(url, output=dir, quiet=False,      # визуализации загрузки 
                                     use_cookies=False # для использования cookies 
                   )
        
        print('Файлы успешно скачаны!')
        return True
    except Exception as e:
        print(f"Ошибка при скачивании с Google Диска:{str(e)}")
        return False
    
    
async def main():
    download_file(file_links)
    
if __name__ == "__main__":
    asyncio.run(main())