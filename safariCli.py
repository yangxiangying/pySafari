#!/Users/localds/my.Venvs/v.py35/bin/python3
# -*- coding: utf-8 -*-
# SB.D.yang - geebook.net
# 20:05 2016年11月6日
# 主题:
import sys
import os
import os.path
import re
import safari
import safariHelp

def plugin():
    os.chdir(plugin_path)
    d = {}
    x = 0
    for f in os.listdir("."):
        if ".py" in f:
            x += 1
            print(x, f.replace(".py", ""))
            d.update({str(x): f})
    exec(open(d[input(">")], 'r').read())


def main():
    #
    if len(sys.argv) == 1:
        print(help())
    elif len(sys.argv) == 2:
        if sys.argv[1] == "source":
            print(safari.source())
        elif sys.argv[1] == "edit":
            safari.edit()
        elif sys.argv[1] == "regex":
            print("\n試試re hh = 常用正則一覽\n")
        elif sys.argv[1] == "moveto":
            print("\n to the right?to the left?\n")
        elif sys.argv[1] == "move":
            print("\n 你想說的是moveto?\n")
        elif sys.argv[1] == "history":
            safari.history()
        elif sys.argv[1] == "dump":
            safari.dump()
        elif sys.argv[1] == "new":
            safari.new()
        elif sys.argv[1] == "plugin":
            plugin()
        elif sys.argv[1] == "tabs":
            safari.tabs()
        elif sys.argv[1] == "ss":
            safari.ss()
        else:
            print("\n不知所云\n")

    elif len(sys.argv) == 3:
        if sys.argv[1] == "re":
            if sys.argv[2] == "hh":
                print(pattern_lst)
            else:
                ptn = sys.argv[2]
                print(safari.re(ptn))
        elif sys.argv[1] == "moveto":
            safari.moveto(sys.argv[2])
        elif sys.argv[1] == "soup.find":
            print(safari.find(sys.argv[2]))
        elif sys.argv[1] == "soup.prettify":
            print(safari.prettify())
        else:
            print("\n雲裡霧裡\n")
    elif len(sys.argv) == 4:
        if sys.argv[1] == "soup.find":
            print(safari.findt(sys.argv[2]))
    else:
        print("爆了")

if __name__ == '__main__':
    main()
