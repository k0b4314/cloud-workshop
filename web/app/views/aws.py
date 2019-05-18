'''
AWSのページを表示する
'''
from flask import Blueprint
from flask import render_template
import app.views.template as template
import app.models.aws as model

view = Blueprint('aws',
                 __name__,
                 url_prefix='/aws')

@view.route('/')
@view.route('/<id>')
def show(id=None):
    if id:
        # 記事単体
        return template.render('aws/show.html', 
                               content=model.get_content(id))
    else:
        # 記事一覧
        return template.render('aws/index.html', 
                               contents_list=model.get_list())

