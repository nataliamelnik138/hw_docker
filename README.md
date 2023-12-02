# Проект платформы для онлайн-обучения

### Технологии:
- Python 3.11
- Django 4.2.2
- Django REST framework 3.14.0
- PostgreSQL
- Celery 5.3.5
- Redis 5.0.1
- Docker

### Инструкция по развертыванию проекта:

Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/hw_docker
```

#### Запуск проекта с использованием Docker:
Запустите контейнер
```
docker-compose up -d —build 
```

#### Запуск проекта без использования Docker:
1. Создайте виртуальное окружение
```
python -m venv venv
```
2. Активируйте виртуальное окружение
```
venv/Skripts/activate
```
4. Установите зависимости
```
pip install -r requirements.txt
```
6. Создайте в папке проекта файл .env, который должен содержать значение переменных из файла .env.sample
7. Примените миграции
```
python manage.py migrate
```
6. Запустите проект
```
python manage.py runserver
```
7. Запустите отложенную задачу отправки письма с информацией об обновлениии материалов курса: 
```
celery -A config worker -l INFO -P eventlet    
```
8. Запустите периодическую задачу блокировки пользователей, не посещающих сервис более 30 дней: 
```
celery -A config  beat -l info 
```

### Документация API
```
http://127.0.0.1:8000/redoc/
```

#### Автор проекта: Мельник Наталья
