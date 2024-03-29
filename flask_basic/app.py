from flask import Flask, render_template

app = Flask(__name__) #アプリケーションオブジェクト __name__：現在のファイルのモジュール名が入る

#View関数
@app.route('/')
def index():
    # return '<h1>Hello World</h1>'
    value = "test"
    return render_template('index.html', value_after=value) #ふつうは=前後は同じ名前

@app.route('/product')
def product():
    product_list = ["computer1","computer2","computer3"]
    product_dict = {"product_name":"computer1","product_price":"30000", "Product_maker":"maker100"}

    return render_template('product.html', products=product_list, product_dict=product_dict)

@app.route('/test')
def test():
    return 'aaa'

@app.route('/user')
def user():
    user_list = [
        ["1", "user1", "aaa@aaa.com", "1"],
        ["2", "user2", "bbb@bbb.com", "0"],
        ["3", "user3", "ccc@ccc.com", "0"],
    ]
    return render_template('user.html', users=user_list)

@app.route('/user/<user_id>')
def userid(user_id):
    return '<h1>ID:{0}</h1>'.format(user_id)
    # return '<h1>ID  :{0} {1} {2}</h1>'.format(user_id[0],user_id[1],user_id[2]) #error


@app.errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404 #カスタマイズしたエラーページ

if __name__ == '__main__': #このファイルをスクリプトとして実行した場合(インポートされた場合の実行を防ぐため、など)
    # app.run(debug=True)
    app.run()

