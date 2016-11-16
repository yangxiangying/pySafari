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
import time



for i in range(100):
    ss = safari.source()
    fanhao_lst = list(set(re.findall("[A-Z]{3,4}\-[0-9]{3}", ss)))
    if len(fanhao_lst) == 0:
        print("可能不在目標頁面"+safari.url)
    else:
        for i in fanhao_lst:
            print("http://www.javpost.net/movie/av/view/"+i)
            os.system(
                "jav -s {fh} -x http://127.0.0.1:8123".format(fh=i))

    time.sleep(30)
