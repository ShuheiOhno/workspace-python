from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dummykey'

class RegistrationForm(FlaskForm):
    email = StringField('メールアドレス')
    username = StringField('ユーザー名')
    password = PasswordField('パスワード')
    pass_confirm = PasswordField('パスワード（確認）')
    submit = SubmitField('登録')

@app.route('/register', method=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.passowrd.data
        return redirect(url_for('user_maintenance'))
    return render_template('register.html', form=form)

@app.route('/user_maintenance')
def user_maintenance():
    return render_template('user_maintenance.html')

if __name__ == '__main__':
    app.run(debug=True)
