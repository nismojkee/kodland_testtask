# KodLand Задание<br><br>
### Поставленное ТЗ

Необходимо написать простой **сайт-блог**, используя технологии, перечисленные в разделе "Стек", и дизайн из макета в Figma.

У сайта должно быть две страницы:

- Главная страница, на которой отображается 10 последних опубликованных постов от свежих к старым. У каждого поста, помимо названия и текста, должны отображаться иллюстрация и  дата публикации. В шапке страницы должна отображаться самая свежая статья.
- Страница для добавления поста с формой, содержащей поле для названия поста, поле для текста поста и поле для загрузки иллюстрации к посту. Здесь пользователь может писать и публиковать свои посты.

В макете на страницах есть много дополнительных иконок и кнопок (а именно: лайки, комменты, просмотры, фильтрация и иконки на навбаре). Их достаточно просто добавить, никакой функционал привязывать к ним не нужно.

Страницу с полным текстом статьи (на которую должна вести, например, кнопка "Читать" в шапке на главной странице) делать **не нужно.**

### Выполнено

Использованы технологии:
1. Python (Django framework)
2. HTML5
3. CSS3 + MDBootstrap (CSS Framework)
4. jQuery + JavaScript

Выполнено:
1. Верстка дизайна средствами Material Design for Bootstrap (MDBootstrap)
2. Обработка событий и вывод необходимого контента:
 - вывод постов (Python Django SQL)
 - добавление нового (Python Django + JavaScript)
3. Публикация поста и его вывод (Python Django SQL)

Работа выволнена согласно поставленного ТЗ и предоставленного макета

### Запуск проекта
1. Установить Python 3.0 или выше
2. Средствами командной строки (Windows) или терминала (Unix) установить:
 - pip
 - Django 3.0 (Django, PIL)
3. После успешной установки перейти средствами командной строки (Windows) или терминала (Unix) в папку с проектом
4. прописать:
 Windows (командная строка):
 - python manage.py makemigrations
 - python manage.py migrate
 - python manage.py runserver<br><br>
 Unix (терминал):
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 - python3 manage.py runserver
5. Перейти в браузере по ссылке https://127.0.0.1:8000
