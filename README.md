Данная программа представляет собой веб-приложение для управления днями рождения сотрудников. Оно позволяет добавлять, редактировать, удалять и просматривать дни рождения сотрудников, а также предоставляет функционал для поиска и сортировки данных. Приложение состоит из нескольких компонентов:
1. Файл add_data.py

    Этот скрипт используется для добавления начальных данных в базу данных. Он содержит список сотрудников с их именами и датами рождения, которые затем добавляются в базу данных с помощью функции add_birthday из модуля database.py.

2. Файл app.py

    Это основной файл веб-приложения, написанный с использованием фреймворка Flask. Он предоставляет REST API для взаимодействия с базой данных и отображения данных на веб-странице. Основные функции:

        Инициализация базы данных: При запуске приложения создается таблица birthdays, если она еще не существует.

        Получение данных: Возвращает список дней рождения, отсортированных по месяцам.

        Добавление данных: Позволяет добавлять новые записи о днях рождения.

        Редактирование данных: Позволяет обновлять существующие записи.

        Удаление данных: Позволяет удалять записи о днях рождения.

3. Файл database.py

    Этот модуль отвечает за взаимодействие с базой данных SQLite. Он содержит функции для:

        Инициализации базы данных и создания таблицы birthdays.

        Получения данных о днях рождения, отсортированных по месяцам.

        Добавления, редактирования и удаления записей.

        Форматирования дат для отображения на веб-странице (например, склонение месяцев).

4. Файл index.html

    Это HTML-шаблон, который отображает интерфейс пользователя. Он включает:

        Таблицу с данными: Отображает список сотрудников и их дни рождения, отсортированные по месяцам.

        Форму для добавления/редактирования: Позволяет добавлять новые записи или редактировать существующие.

        Поиск: Поле для поиска сотрудников по имени.

        Уведомление о ближайшем дне рождения: Показывает уведомление с информацией о ближайшем дне рождения через 3 секунды после загрузки страницы.

Основные функции приложения:

    Сортировка по месяцам: Дни рождения сотрудников сортируются по месяцам и отображаются в виде таблицы с заголовками месяцев.

    Поиск по имени: Пользователь может искать сотрудников по имени, и таблица будет автоматически фильтроваться.

    Добавление/редактирование/удаление: Пользователь может добавлять новые записи, редактировать существующие или удалять их.

    Уведомление о ближайшем дне рождения: При загрузке страницы появляется уведомление с информацией о ближайшем дне рождения сотрудника.

Технологии:

    Flask: Используется для создания веб-приложения и обработки HTTP-запросов.

    SQLite: Используется для хранения данных о днях рождения сотрудников.

    Bootstrap: Используется для стилизации интерфейса и создания адаптивного дизайна.

    JavaScript: Используется для динамического обновления данных на странице, обработки событий и отображения уведомлений.

Как работает приложение:

    При запуске приложения инициализируется база данных, и создается таблица birthdays, если она еще не существует.

    Пользователь может добавлять, редактировать и удалять записи о днях рождения через веб-интерфейс.

    Данные отображаются в виде таблицы, отсортированной по месяцам, с возможностью поиска по имени.

    При загрузке страницы появляется уведомление о ближайшем дне рождения сотрудника.

Это приложение может быть полезно для компаний, которые хотят отслеживать дни рождения своих сотрудников и своевременно поздравлять их.
Для полного контроля можно добавить форму авторизации, чтобы редактировать данные могли не все, а только отдел кадров к примеру.
