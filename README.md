# Приватные заметки пользователя Diary
Приложение для сохранения приватных заметок пользователя.

Стек
Python 3
Django
PostgreSQL
bootstrap4
django-ckeditor для html форматирования заметок
django-currentuser для выбора текущего пользователя при формировании запросов


Функциональные возможности
Пользователь может зарегистрироваться в сервисе задав пару электропочта-пароль
В системе может существовать много пользователей
Пользователь может авторизоваться в сервисе предоставив пару электропочта-пароль
Пользователь видит только свои заметки
На главной странице отображается количество заметок пользователя
Пользователь может создать заметки. Заметка содержит следующие обязательные поля:

- Название (поле text)
- Время создания (поле created_on)

### Деплой

Использован gunicorn + nginx.

1. Переименуйте *.env.prod-sample* в *.env.prod*,
а *.env.prod.db-sample* в *.env.prod.db*.
2. При необходимости обновите пременные окружения.
3. Создайте образ, проведите миграции и запустите.

```sh
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml up
```

Проект будет доступен по адресу [http://localhost:4000](http://localhost:4000)
