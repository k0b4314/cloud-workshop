'''
GCP記事
'''

contents = [
    {
        'id' : '0',
        'title' : 'Webアプリケーションを構築してみる',
        'entry' : '''
            GCPを使ってWebアプリケーションを構築してみます。   
            使うサービス   
            - Compute Engine   
            - App Engine   
            - Cloud Functions   
        ''',
        'released_at' : '2019-01-01',
        'author_names' : 'moon0711mukh'
    },
    {
        'id' : '1',
        'title' : 'データウェアハウスを構築してみる',
        'entry' : '''
            GCPを使ってデータウェアハウスを構築してみます。   
            使うサービス   
            - Cloud Storage   
            - BigQuery   
              
              
              
            BigQueryってなに？  
              
            BigQueryとは、GCPが提供する、データウェアハウスサービスです。
        ''',
        'released_at' : '2019-01-01',
        'author_names' : 'moon0711mukh'
    },
    {
        'id' : '2',
        'title' : 'サーバレスでアプリケーションを動かしてみる',
        'entry' : '''
            GCPを使ってサーバレスでアプリケーションを動かしてみます。   
            使うサービス   
            - Cloud Functions   
              
            Cloud Functionsとは  
              
            ソースコードをデプロイし、サーバレスでアプリケーションを動かします。  
            HTTPリクエスト、ストレージにファイル配置などをトリガーに実行できます
        ''',
        'released_at' : '2019-01-01',
        'author_names' : 'moon0711mukh'
    },    
]


def get_list():
    return contents

def get_content(id):
    return contents[int(id)]
