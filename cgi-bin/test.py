#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

import look

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
    print html % look.look(action)
else:
    print html


