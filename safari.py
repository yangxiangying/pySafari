#!/Users/localds/my.Venvs/v.py35/bin/python3
# -*- coding: utf-8 -*-
# SB.D.yang - geebook.net
# 21:20 2016年11月5日
# 主题:
import sys
import os
import os.path
import re as RE
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import unquote
import conf
# os.chdir(".")

dump_to = "/Users/localds/Websites/sites.网站收藏夹/"


def dump():
    try:
        os.mkdir("{dump_to}{netloc}".format(dump_to=dump_to, netloc=netloc()))
    except:
        next
def dump_source():
    # 使用applescipt 將網頁保存到temp
    os.system("""osascript -e 'tell application "Safari" to return source of front document'>{file}""".format(file=conf.temp_file_path))

def source():
    # 取得源碼
    dump_source()
    return open(conf.temp_file_path, 'r').read()

def edit():
    # 開發功能 用編輯器打開
    os.system(conf.edit)

def lst_printer(lst):
    for i in lst:
        print(i)


def history():
    net_loc_lst = []
    for i in os.listdir(safari_history_path):
        url = unquote(i)
        o = urlparse(url)
        net_loc_lst.append(o.netloc)


def moveto(where):
    if where not in ['left', 'right']:
        print("只有左右哦")
    else:
        d = {}
        d['left'] = movetoleft
        d['right'] = movetoright
        os.system(d[where])


def new():
    os.system(new)


def tabs():
    os.system(tabs)
# 改變窗口大小


def size(x, y):
    t = """osascript -e 'tell application "Safari" to set bounds of window 1 to {50, 50, 1000, 1000}'"""


def ss():
    os.system(safari_source)





def down():
    os.system("mv .temp ~/desktop/temp.html")


def netloc():
    return urlparse(url()).netloc


def url():
    os.system(gettemp)
    return source().replace("\n", "")


def re(pattern):
    return RE.findall(pattern, source())


def findt(tag):
    try:
        return [i.text for i in soup().find(id=tag)]
    except:
        return [i.text for i in soup().select(".{tag}".format(tag=tag))]


def find(tag):
    try:
        return [i for i in soup().find(id=tag)]
    except:
        return [i for i in soup().select(".{tag}".format(tag=tag))]


def soup():
    return BeautifulSoup(source(), 'lxml')
