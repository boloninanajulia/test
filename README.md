# Test. Тестовый проект. API поддерживающее CRUD запросы 2х связанных таблиц departments и employees

Requirements:
- Python 3.7

Быстрый старт:
- Настроить виртуальную среду virtualenv
- Перейти в папку проекта
- Выполнить установку зависимостей:
    - pip install -r requirements.txt
- Настроить переменные среды:
    - export FLASK_APP=./wsgi.py
    - export FLASK_ENV=prod
    - export FLASK_DEBUG=0
- Создание базы данных и выполнение миграций:
    - flask db init
    - flask db migrate
    - flask db upgrade

Запуск:
- flask run
