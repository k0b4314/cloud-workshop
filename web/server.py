'''
ローカル環境　Webアプリケーション起動元
'''
import os
import app.app as app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
