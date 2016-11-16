#!/Users/localds/my.Venvs/v.py35/bin/python3
# 激活
#
import os

home_path = os.environ['HOME']

app_name = "Safari"

app_root_path = os.path.join(home_path, app_name)

temp_file_name = '.safaritemp'
temp_file_path = os.path.join(home_path, temp_file_name)



edit = 'subl {path}'.format(path=app_root_path)


osa_run = """osascript -e """
# 開心
reset = """osascript -e 'tell application "Safari" to make new document'"""
movetoleft = """osascript -e 'tell application "Safari" to set bounds of window 1 to {50, 50, 1000, 1000}'"""
movetoright = """osascript -e 'tell application "Safari" to set bounds of window 1 to {1000, 50, 1920, 1000}'"""
plugin_path = """/Users/localds/my.Venvs/v.py35/lib/python3.5/site-packages/Safari/plugin"""
tabs = """osascript -e 'tell application "Safari" to get tabs as list'"""

safari_history_path = """/Users/localds/Library/Caches/Metadata/Safari/History/"""
conf_file = """/Users/localds/doing/doing.Safari/Safari/conf.py"""

safari_activate = osa_run + """'tell application "Safari" to activate'"""
safari_version = osa_run + """'tell application "Safari" to return version'"""


t = osa_run + """'tell application "Safari" to activate'"""
