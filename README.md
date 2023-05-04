## DjangoQuiz

DjangoQuiz - это веб-приложение, построенное на Django, которое позволяет пользователям создавать и проходить тесты.

### Возможности
- Аутентификация пользователя
- Создание тестов с вопросами с выбором из нескольких вариантов ответа
- Прохождение тестов и получение мгновенной обратной связи
- Просмотр результатов прошлых тестов

### Установка

1. Склонируйте репозиторий
```
git clone https://github.com/Ivan-k35/DjangoQuiz.git
```

2. Установите необходимые зависимости
```
pip install -r requirements.txt
```

3. Примените миграции базы данных
```
python manage.py migrate
```

4. Запустите сервер
```
python manage.py runserver
```

### Использование
1. Зарегистрируйтесь или войдите в существующую учетную запись.
2. Создайте тест и добавьте вопросы.
3. Пройдите тест и получите мгновенную обратную связь по ответам.
4. Просмотрите свои результаты прошлых тестов.
