# just-python-code

Проект по работе с 

<h1 align="center">just-python-code</h1>

<h2 align="center">Используемые библиотеки</h2>

<div align="center">

<a href="https://www.python.org" target="_blank" rel="noreferrer" style="display: inline-block;"> 
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/>
</a>

<a href="pytest" target="pytest" rel="noreferrer"> 
    <img src="https://docs.pytest.org/en/stable/_static/pytest1.png" alt="pytest" width="60" height="60"/> 
</a>

</div>


### 1. Клонируй проект и перейди в папку
```bash
git clone git@github.com:TUBE-GULL/just-python-code.git

cd just-python-code
```

## 2. Установка Зависимостей 

```bash
pip install pytest 

```
## или Установить с помощью файла `requirements.txt` 
```bash
pip install -r requirements.txt

```

## 3. Запуск 
```bash
python src/main.py ./downloads/data1.csv ./downloads/data2.csv --report report
python src/main.py ./downloads/data1.csv ./downloads/data2.csv --report payout 
python src/main.py ./downloads/data1.csv ./downloads/data2.csv --report bonus
```
![ожидаемый результат report](img/report.png)
![ожидаемый результат payout](img/payout.png)
![ожидаемый результат bonus](img/bonus.png)
![в случае неверно введенной команды](img/error.png)



### 3. Тестирование
```bash
pytest
```

![результат теста](img/test.png)
