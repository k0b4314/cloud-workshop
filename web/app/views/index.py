'''
indexを表示する
'''
from flask import Blueprint
from flask import render_template
import app.views.template as template

view = Blueprint('index',
                 __name__,
                 url_prefix='/')

@view.route('/')
def show():
    return template.render('index.html',
                           content="クラウド勉強会用デモページです")