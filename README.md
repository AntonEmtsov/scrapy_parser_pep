# scrapy_parser_pep
# Проект парсинга pep

### Тенологии используемые в проекте:
- python 3.8
- Scrapy 2.5.1

### Как запустить проект:
Клонировать репозиторий:
```
git clone https://github.com/russ044/scrapy_parser_pep.git
```
Создать и активировать виртуальное окружение:
```
python -m venv venv
.\venv\Scripts\activate
```
Установить зависимостей:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Запустить парсер:
```
scrapy crawl pep
```
### Пример работы:

Создается два файла с результатами парсинга:
 - ```pep_data_time.csv```  все существующие PEP с их номером, названием и статусом.
 - ```status_summary_data_time.csv``` сумма по каждому статусу и их общее количество.
pep_data_time.csv
```
number,name,status
1,PEP Purpose and Guidelines,Active
214,Extended Print Statement,Final
215,String Interpolation,Superseded
211,Adding A New Outer Product Operator,Rejected
...
```

status_summary_data_time.csv
```
Статус,Колличество
Accepted,44
Active,31
April Fool!,1
Deferred,36
Draft,31
...
```
### Автор проекта:
- Емцов А.В.  [russ044](https://github.com/russ044)
