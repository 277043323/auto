import flask
from flask import Flask
import flask_login
app = Flask(__name__)
app.secret_key='supe secret string'
login_manager = flask_login.LoginManager()

login_manager.init_app(app)
users = {'foo@bar.tld': {'password': 'secret'},'277043323@qq.com':{'password':123456}}
class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
               <label>用户邮箱:</label>
                <input type='text' name='email' id='email' placeholder='email'/>
                <label>用户密码:</label>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"