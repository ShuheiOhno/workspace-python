from flask import Flask

app = Flask(__name__) #アプリケーションオブジェクト __name__：現在のファイルのモジュール名が入る

#View関数
@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/test')
def test():
    return 'aaa'

@app.route('/user/<user_id>')
def userid(user_id):
    return '<h1>ID:{0}</h1>'.format(user_id)
    # return '<h1>ID  :{0} {1} {2}</h1>'.format(user_id[0],user_id[1],user_id[2]) #error

if __name__ == '__main__': #このファイルをスクリプトとして実行した場合(インポートされた場合の実行を防ぐため、など)
    # app.run(debug=True)
    app.run()

