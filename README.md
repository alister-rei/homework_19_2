# Aleksey Khadkov

## Для подключения к базе данных создать файл `database.ini`, добавить в него : user, password, host,

## Для быстрой загрузки категорий и продуктов в таблице используйте `python manage.py loaddata catalog_data.json`

## В файле `config/settings.py` заменить `EMAIL_HOST_USER = 'your_email@yandex.ru' EMAIL_HOST_PASSWORD = 'your_yandex_smtp_password'` на свои данные

## В файле `user/management/commands/csu.py` команда для создания суперпользователя с паролем

## Homework 22.2 :

- 1 Добавлены пользователи с регистрацией по почте и полями профиля «Аватар», «Номер телефона», «Страна» итд.
- 2 регистрация происходит с подтверждением по почте
- 3 реализована авторизация пользователя
- 4 есть способ изменения пароля через почту
- 5 для анонимных пользователей закрыты все контроллеры, которые отвечают за работу с продуктами. При этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.




