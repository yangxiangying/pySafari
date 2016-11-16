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
import requests



def eff():
	from bs4 import BeautifulSoup
	import requests
	content = safari.source()
	to_lst=[]
	if "&page=" in safari.url():
		u = safari.url().split("&page=")[0]
		to_lst = [u+"&page="+str(i) for i in range(0,400)]
	soup = BeautifulSoup(content,'lxml')
	#d={}
	#for i in soup.select(".root"):
	#	d.udpate({i.a.get("href"):i.text})
	res = soup.select("h2.a-size-base")[0].text.strip()
	print(res)
	p=res.split("results for")
	amazon_class = p[1] 
	p=p[0].split("of")
	perpage = int(p[0].split("-")[1])
	total= int(p[1].replace(",",""))
	num_of_page = total//perpage
	print(num_of_page)
	foo = open("temp.html",'w')
	n = 400
	for i in to_lst:
		r=requests.get(i)
		n -= 1
		target=BeautifulSoup(r.content ,'lxml').select("#search-results")
		foo.write(str(target))
		print(n)
	foo.close()


		


eff()



