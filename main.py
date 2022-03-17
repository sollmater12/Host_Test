from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promotion():
    check = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(check)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')