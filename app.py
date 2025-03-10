from flask import Flask, render_template, request, jsonify
import database  # Импортируем наш модуль для работы с базой данных

app = Flask(__name__)

# Инициализация базы данных при запуске приложения
database.init_db()

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Получить все дни рождения, отсортированные по месяцам
@app.route('/birthdays/sorted', methods=['GET'])
def get_birthdays_sorted():
    birthdays = database.get_birthdays_sorted_by_month()
    return jsonify([dict(birthday) for birthday in birthdays])

# Добавить новый день рождения
@app.route('/birthdays', methods=['POST'])
def add_birthday():
    data = request.json
    database.add_birthday(data['name'], data['birthday'])
    return jsonify({"message": "Запись добавлена"}), 201

# Редактировать день рождения
@app.route('/birthdays/<int:id>', methods=['PUT'])
def update_birthday(id):
    data = request.json
    database.update_birthday(id, data['name'], data['birthday'])
    return jsonify({"message": "Запись обновлена"})

# Удалить день рождения
@app.route('/birthdays/<int:id>', methods=['DELETE'])
def delete_birthday(id):
    database.delete_birthday(id)
    return jsonify({"message": "Запись удалена"})

if __name__ == '__main__':
    # В данном примере программа запустится на localhost по стандартному порту 5000
    app.run(host='localhost', port=5000, debug=True)
