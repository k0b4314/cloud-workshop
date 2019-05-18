'''
GCPのページを表示する
'''
from flask import Blueprint
import app.views.template as template
import app.models.gcp as model

view = Blueprint('gcp',
                 __name__,
                 url_prefix='/gcp')

@view.route('/')
@view.route('/<id>')
def show(id=None):
    if id:
        # 記事単体
        return template.render('gcp/show.html', 
                               content=model.get_content(id))
    else:
        # 記事一覧
        return template.render('gcp/index.html', 
                               contents_list=model.get_list())


