#!/usr/bin/env python3

'''
 File:         redir.py
 Created:      261117
 Description:  Initial redirection (developing a proper CV website can take lots of time)
'''

from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route('/')
def linkedin():
 return redirect("https://www.linkedin.com/in/antoniodellelce")


## EOF ##

