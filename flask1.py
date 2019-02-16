from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# Чтобы добавлять к адресу URL переменные части, можно эти особые части выделить как <variable_name>.
# Затем подобные части передаются в вашу функцию в качестве аргумента - в виде ключевого слова.
# Также может быть использован конвертер - с помощью задания правила следующего вида <converter:variable_name>.
# Вот несколько интересных примеров

# Существуют следующие конвертеры:
# int - принимаются целочисленные значения
# float - как и int, только значения с плавающей точкой
# path - подобно поведению по умолчанию, но допускаются слэши


@app.route('/user/<username>')
def show_user_profile(username):
    # показать профиль данного пользователя
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id

# Для построения URL для специфической функции, вы можете использовать функцию url_for().
# В качестве первого аргумента она принимает имя функции, кроме того она принимает ряд именованных аргументов,
# каждый из которых соответствует переменной части правила для URL. Неизвестные переменные части добавляются к URL в
# качестве параметров запроса. Вот некоторые примеры:


with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('show_post', post_id='56'))
    print(url_for('show_user_profile', username='John Smith'))








if __name__ == '__main__':
    app.run(debug=True)  # Опция debug включает перезагрузку сервера при изменении кода.
