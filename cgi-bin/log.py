#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cgi

form = cgi.FieldStorage()
if form.has_key('file'):
    action = form['file'].value
else:
    print """
        <!DOCTYPE html>
        """

f = open(action)
contents = f.read()
f.close()

print """
<!DOCTYPE html>
%s
""" % (contents)
