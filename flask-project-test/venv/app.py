from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!!!!'

@app.route('/hello2')
def hello2():
    return 'Hello, World2'

@app.route('/hello3')
def hello3():
    return 'Hello, World!3'

# ルーティング（共通部分あり） 可変式
@app.route("/japan/<city>")
def tokyo(city):
    return f"Hello, {city} in Japan!!!"

# ｈｔｍｌ テンプレートファイル
@app.route("/html")
def html():
    return render_template('hello.html')