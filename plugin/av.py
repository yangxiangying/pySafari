#!/Users/localds/my.Venvs/v.py35/bin/python3
# -*- coding: utf-8 -*-
# SB.D.yang - geebook.net
# 20:05 2016年11月6日
# 主题:

import sys
import os
import os.path
import re
import json
from Safari import safari
from bs4 import BeautifulSoup





def main(fanhao_lst, pkl_file):
    import pickle
    pk_data = {}
    to_down_lst = []

    for fanhao in fanhao_lst:
        try:
            json_file = "/Users/localds/AV/{fanhao}/{fanhao}.json".format(
                fanhao=fanhao)
            # print(json_file)
            json_data = open(json_file, 'r').read()
            dic = eval(json_data)
            print(fanhao)
            print(dic['actress'])
            print(dic['category'])
            
            print("\n==========\n")
        except:
            to_down_lst.append(fanhao)
            # os.system(
            #    "jav -s {fh} -x http://127.0.0.1:8123".format(fh=fanhao))
    pk_data['todown'] = to_down_lst
    with open(pkl_file, 'wb') as f:
        pickle.dump(pk_data, f, pickle.HIGHEST_PROTOCOL)

    # seek(fanhao_lst)


path = "/Users/localds/AV/"
pkl_file = path + ".data.pkl"

os.chdir(path)
flst = [f for f in os.listdir(".") if ".DS" not in f]
print("庫存量{n}".format(n=len(flst)))

d = {}

ss = safari.source()
soup = BeautifulSoup(ss,'lxml')
playing = [t.text for t in soup.findAll("h3")][0]
playing_fanhao = re.findall("[A-Z]{3,4}\-[0-9]{3}", playing)
print(playing)
main(playing_fanhao, pkl_file)
print("=-=-=-=-=-=-=-=-=-=-=\n")
# print(ss)

fanhao_lst = list(set(re.findall("[A-Z]{3,4}\-[0-9]{3}", ss)))
if len(fanhao_lst) == 0:
    print("可能不在目標頁面")
main(fanhao_lst, pkl_file)
