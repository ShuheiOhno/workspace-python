from flask import Flask

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

# ルーティング（共通部分あり）
@app.route("/japan/<city>")
def tokyo(city):
    return f"Hello, {city} in Japan!!!"