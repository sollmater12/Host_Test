from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def main():
    return '<link rel="icon" href="#"><h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<link rel="icon" href="#"><h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def promotion():
    check = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '<link rel="icon" href="#">' + str('</br>'.join(check))


if __name__ == '__main__':
    port = int(os.environ.get("POST", 5000))
    app.run(host="0.0.0.0", port=port)

