from flask import Flask

app = Flask(__name__) #アプリケーションオブジェクト __name__：現在のファイルのモジュール名が入る

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__': #このファイルをスクリプトとして実行した場合(インポートされた場合の実行を防ぐため、など)
    app.run()

