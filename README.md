# metro-app



## Installation
- Склонировать репозиторий
- При первом запуске загрузить данные в базу !!! База уже лежит в гите, поэтому сейчас нет необходимости 
  - (При большом желании сначала удалить data.db в корне, только потом запустить)
  - Занимает около 5 минут
- Запустить api сервер
- Выполнить клиентский код

Сервер:
```bash
    git clone ...
    cd metro-app
    python3 src/load.py
    python3 src/api.py
```
Клиент:
```bash
    python3 client.py
```

## Requirements
- python >= 3.10

## Development
### Server
#### Load
    1. Исходные данные хранятся в каталоге data.
    2. Инициалищируется база данных sqlite - схема: src/database/schema.sql
    3. Модели данных - src/models/{house, metro} - датаклассы для хранения - без логики
    4. Парсятся файлы с данными: классы генераторы src/parsers/{house_parser, metro_parser}
        - house_parser возвращает по одному объекту House
        - metro_parser возврашает плоский список станций для всего городского метро
    5. Загрузчики - src/loaders/{house_loader, metro_loader}. 
        - house_loader неявно накапливает в себе список домов и при достижении лимита пишет в базу
        - metro_loader записывает сразу
    6. Собираются аггрегированные таблицы статистики по станциям: src/database/aggregate (sql)
#### API
    1. Использует сокеты 
    2. Слушает запросы вида {"method": "get", "filters": {"metro_name": "Самара"}}
    3. Вызывает src/readers/metro_readaer, который возвращает данные из таблиц статистики
    4. Возвращает bytes(json) вида "data": [[--station-info--], [--station2-info--]]

### Client
    1. Посылает запрос на api сервер
    2. Получает список станций по фильтру
    3. Обрабатывает...
