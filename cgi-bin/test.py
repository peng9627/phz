#! /usr/bin/python
# -*- coding: utf-8 -*-
import cgi

import look1

print("Content-type: text/html;charset=utf-8\n\n")

html = '''
    <!DOCTYPE html>
    '''
form = cgi.FieldStorage()
if form.has_key('action'):
    action = form['action'].value
    html = '''
    <!DOCTYPE html>
    %s
    '''
    print html % look1.look(action)
else:
    print html
