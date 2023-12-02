# Проект платформы для онлайн-обучения

### Инструкция по запуску:

Клонирование проекта:
```
git clone https://github.com/nataliamelnik138/hw_docker
```
Запуск:
1. Сборка образов
```
docker-compose build 
```
2. Запуск контейнеров
```
docker-compose up
```
3. Применнение миграции
```
docker-compose exec app python manage.py migrate
```

#### Автор проекта: Мельник Наталья
