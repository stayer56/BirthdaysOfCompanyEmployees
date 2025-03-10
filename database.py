import sqlite3
from datetime import datetime
import locale
import sys

if sys.platform == 'win32':
    locale.setlocale(locale.LC_TIME, 'Russian_Russia.1251')  # Для Windows
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')  # Для Linux

# Словарь для склонения месяцев
MONTHS = {
    "январь": "января",
    "февраль": "февраля",
    "март": "марта",
    "апрель": "апреля",
    "май": "мая",
    "июнь": "июня",
    "июль": "июля",
    "август": "августа",
    "сентябрь": "сентября",
    "октябрь": "октября",
    "ноябрь": "ноября",
    "декабрь": "декабря",
}

def get_db_connection():
    conn = sqlite3.connect('birthdays.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS birthdays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_birthdays_sorted_by_month():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Сортируем по месяцу и дню
    cursor.execute('SELECT * FROM birthdays ORDER BY SUBSTR(birthday, 6, 2), SUBSTR(birthday, 9, 2)')
    birthdays = cursor.fetchall()
    conn.close()

    # Форматируем даты
    formatted_birthdays = []
    for birthday in birthdays:
        date_obj = datetime.strptime(birthday['birthday'], '%Y-%m-%d')
        month_name = date_obj.strftime('%B').lower()  # Получаем название месяца в нижнем регистре
        month_name_declined = MONTHS.get(month_name, month_name)  # Склоняем месяц
        formatted_date = date_obj.strftime('%d ') + month_name_declined  # Формат: "01 ноября"
        formatted_birthdays.append({
            "id": birthday['id'],
            "name": birthday['name'],
            "birthday": formatted_date,  # Отформатированная дата для отображения
            "original_birthday": birthday['birthday']  # Исходная дата для сортировки
        })
    
    return formatted_birthdays

# Добавление нового дня рождения
def add_birthday(name, birthday):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO birthdays (name, birthday) VALUES (?, ?)', (name, birthday))
    conn.commit()
    conn.close()

# Редактирование дня рождения
def update_birthday(id, name, birthday):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE birthdays SET name = ?, birthday = ? WHERE id = ?', (name, birthday, id))
    conn.commit()
    conn.close()

# Удаление дня рождения
def delete_birthday(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM birthdays WHERE id = ?', (id,))
    conn.commit()
    conn.close()