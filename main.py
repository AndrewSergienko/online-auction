import os
from bottle import template, static_file, abort, request, SimpleTemplate, redirect, \
    Bottle

from models import Lot, User
from bottle_login import LoginPlugin

from datetime import datetime
from sqlite3 import OperationalError

# from redis import Redis
# redis = Redis(host='localhost', port=6379, db=0)

app = Bottle()
app.config['SECRET_KEY'] = 'secret'
login = app.install(LoginPlugin())


@app.hook('before_request')
def _context_processor():
    SimpleTemplate.defaults['request'] = request


@app.route('/register', method='GET')
@app.route('/register', method='POST')
def register():
    if request.method == 'POST':
        user = User(**request.forms)
        user.set_password(request.forms['password'])
        user.save()
        redirect('/login')
    return template('register.tpl')


@app.route('/login', method='GET')
@app.route('/login', method='POST')
def signin():
    if request.method == 'POST':
        user = User.get(username=request.forms['username'])
        if not user:
            return 'User don\'t exist'
        if not user.check_password(request.forms['password']):
            return 'Password is not correct'
        login.login_user(user.id)
        return 'Success'
    return template('login.tpl')


@app.route('/logout')
def signout():
    login.logout_user()
    redirect('/login')


@login.load_user
def load_user_by_id(user_id):
    user = User.get(id=user_id)
    return user


@app.route('/')
def dashboard():
    print(login.get_user())
    now = datetime.now()
    lots = Lot.all()
    context = {'default_picture': 'no_image.jpg',
               'lots': lots,
               'now': now}
    return template('lots.tpl', context)


@app.route('/lot/<lot_id>')
def lot_info(lot_id):
    lot = get_or_404(Lot, id=lot_id)
    dirname = f'media/lots/{lot.picture_path}'
    pictures = os.listdir(dirname)
    context = {'lot': lot, 'pictures': pictures}
    return template('lot_info.tpl', context)


@app.route('/static/<static:path>', name='static')
def server_static(static):
    return static_file(static, root='views/static/')


@app.route('/media/<media:path>', name='media')
def server_media(media):
    return static_file(media, root='media/')


@app.error(404)
def error_404(error):
    return template('404.tpl')


def get_or_404(cls, **kwargs):
    try:
        obj = cls.get(**kwargs)
        return obj
    except OperationalError:
        abort(404)


app.run(host='localhost', port=8080)