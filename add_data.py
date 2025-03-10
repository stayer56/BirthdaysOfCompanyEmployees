import database

# Данные для добавления
employees = [
    {"name": "ФИО", "birthday": "ГОД-МЕСЯЦ-ДЕНЬ"},
    # Добавьте остальные данные
]

# Добавление данных в базу
for employee in employees:
    database.add_birthday(employee["name"], employee["birthday"])

print("Данные успешно добавлены!")