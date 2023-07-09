# Онлайн-платформа торговой сети электроники

Веб-приложение с API-интерфейсом и админ-панелью
Стек технологий: Python 3.11, Django 4.2.1, Postgres

<h3>Запуск проекта</h3>

1. Создать виртуальное окружение
`python3 -m venv venv`
2. Активировать виртуальное окружение
`venv/Scripts/activate (Windows)
source venv/bin/activate (MacOS)`
2. Установить зависимости
`pip install -r requirements.txt`
3. Создать и накатить миграции:
 - `./manage.py makemigrations`
 - `./manage.py migrate`
4. Запустить проект:
- `./manage.py runserver`
