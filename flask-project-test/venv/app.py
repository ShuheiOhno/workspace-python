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

# テンプレートに値を渡す
@app.route("/valuesend/<value>/<secondvalue>")
def valuesend(value, secondvalue):
    return render_template("hello.html", val=value,secondval=secondvalue)

# テンプレートに値を渡す(配列使用)
arr = ['値1','値2','値3','値4','値5','値6','値7','値8','値9']

@app.route("/array")
def valuesend():
    return render_template("hello.html", elements=arr)