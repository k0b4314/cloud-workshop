'''
Webサイトを表示する
'''

from flask import render_template

def create_site_menu():
    '''サイトバーを作成
    
    Returns:
        str -- side_menu
    '''
    menu = [
        {'route' : 'gcp', 'name' : 'Google Cloud Platform'},
        {'route' : 'aws', 'name' : 'Amazon Web Service'},
        {'route' : 'azure', 'name' : 'Microsoft Azure'},
        {'route' : 'help', 'name' : 'Help'},
        {'route' : '', 'name' : 'Top'},
    ]
    side_menu = '<form action="#" method="post">'
    for v in menu:
        side_menu += '<button class="menu-button" type="button">' \
                     '  <a href="/{route}" class="menu-text">{name}</a>' \
                     '</button>'.format(route=v['route'], name=v['name'])
    side_menu += '</form>'
    return side_menu


def render(template, content=None, contents_list=None):
    '''jinja2テンプレートをレンダリングし、htmlを返す
    
    Arguments:
        template {str} -- templateファイルのパス
    
    Keyword Arguments:
        content {object} -- コンテンツ
        contents_list {list} -- コンテンツリスト
    
    Returns:
        html
    '''
    return render_template(template, 
                           content=content,
                           contents_list=contents_list,
                           side_menu=create_site_menu())
