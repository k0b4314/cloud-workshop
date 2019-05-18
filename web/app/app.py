'''
Webアプリケーションを起動する
'''

from flask import Flask
from app.views import index
from app.views import aws
from app.views import gcp

# ルーティング設定
app = Flask(__name__)
app.register_blueprint(index.view)
app.register_blueprint(gcp.view)
app.register_blueprint(aws.view)

def run(host=None, port=None):
    app.run(host=host, port=port)

