import os
from bottle import route, run, template, static_file, error, abort, request, auth_basic, SimpleTemplate, hook

from models import Lot

from datetime import datetime
from sqlite3 import OperationalError

# from redis import Redis
# redis = Redis(host='localhost', port=6379, db=0)


@hook('before_request')
def _context_processor():
    SimpleTemplate.defaults['request'] = request


def check_auth(user, pw):
    pass


@route('/')
def dashboard():
    now = datetime.now()
    lots = Lot.all()
    lots = list(map(create_time_object, lots))
    context = {'default_picture': 'no_image.jpg',
               'lots': lots,
               'now': now}
    return template('lots.tpl', context)


def create_time_object(lot: Lot):
    lot.start_object_time = datetime.strptime(f"{lot.start_date} {lot.start_time}", "%d.%m.%Y %H:%M")
    lot.end_object_time = datetime.strptime(f"{lot.end_date} {lot.end_time}", "%d.%m.%Y %H:%M")
    return lot


@route('/lot/<lot_id>')
def lot_info(lot_id):
    lot = get_or_404(Lot, id=lot_id)
    dirname = f'media/lots/{lot.picture_path}'
    pictures = os.listdir(dirname)
    context = {'lot': lot, 'pictures': pictures}
    return template('lot_info.tpl', context)


@route('/static/<static:path>', name='static')
def server_static(static):
    return static_file(static, root='views/static/')


@route('/media/<media:path>', name='media')
def server_media(media):
    return static_file(media, root='media/')


@error(404)
def error_404(error):
    return template('404.tpl')


def get_or_404(cls, **kwargs):
    try:
        obj = cls.get(**kwargs)
        return obj
    except OperationalError:
        abort(404)


run(host='localhost', port=8080)