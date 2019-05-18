'''
AWS記事
'''

contents = [
    {
        'id' : '0',
        'title' : 'Webアプリケーションを構築してみる',
        'entry' : '''
            AWSを使ってWebアプリケーションを構築してみます。   
            - hoge  
            - hoge  
            - hoge  
            - hoge  
            - hoge  
            - hoge  
        ''',
        'released_at' : '2019-01-01',
        'author_names' : 'moon0711mukh'
    },
    {
        'id' : '1',
        'title' : 'データウェアハウスを構築してみる',
        'entry' : '''
            GCPを使ってデータウェアハウスを構築してみます。   
            - hoge  
            - hoge  
            - hoge  
            - hoge  
            - hoge  
            - hoge  
        ''',
        'released_at' : '2019-01-01',
        'author_names' : 'moon0711mukh'
    },
]


def get_list():
    return contents

def get_content(id):
    return contents[int(id)]
