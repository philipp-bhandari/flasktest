from flask import Flask, url_for, request, render_template
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
# Чтобы сформировать для статических файлов URL, используйте специальное окончание 'static':
    print(url_for('static', filename='style.css'))

# HTTP (протокол, на котором общаются веб-приложения) может использовать
# различные методы для доступа к URL-адресам. По умолчанию, route отвечает
# лишь на запросы типа GET, но это можно изменить, снабдив декоратор route()
# аргументом methods. Вот некоторые примеры:


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass  # Логинимся
    else:
        pass  # показываем форму логина

# Flask будет искать шаблоны в папке templates.
# Поэтому, если ваше приложение выполнено в виде модуля, эта папка будет рядом с модулем,
# а если в виде пакета, она будет внутри вашего пакета:
#
# Первый случай - модуль:
#
# /application.py
# /templates
#     /hello.html
#
# Второй случай - пакет:
#
# /application
#     /__init__.py
#     /templates
#         /hello.html


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)




if __name__ == '__main__':
    app.run(debug=True)  # Опция debug включает перезагрузку сервера при изменении кода.

