#!usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import cgitb
import sys

cgitb.enable()

form = cgi.FieldStrorage()


print("Content-Type: text/html; charset=UTF-8")
print("")


if "text" not in form:
	print("<h1>Error!</h1>")
	print("<br>")
	print("テキストを入力してください")
	print("<a href='/'><button type='submit'>戻る</button></a>")
	sys.exit()


text = form.getvalue(text)

print(text)