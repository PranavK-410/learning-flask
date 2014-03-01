#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FILE: hello.py
# AUTHOR: haya14busa
# License: MIT license
#
#     Permission is hereby granted, free of charge, to any person obtaining
#     a copy of this software and associated documentation files (the
#     "Software"), to deal in the Software without restriction, including
#     without limitation the rights to use, copy, modify, merge, publish,
#     distribute, sublicense, and/or sell copies of the Software, and to
#     permit persons to whom the Software is furnished to do so, subject to
#     the following conditions:
#
#     The above copyright notice and this permission notice shall be included
#     in all copies or substantial portions of the Software.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#     OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#     MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#     CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#     TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#=============================================================================

''' Import the Flask class.
An Instance of this class will be our WSGI application
'''
from flask import Flask

''' Create an instance of this class.
The first argument is the name of the application's module or package.
Single module -> `__name__`
This is needed so that Flask knows where to look for templates, static files,
and so on
'''
app = Flask(__name__)


# Use the `route()` decorator
# to tell Flask what URL should trigger our function
@app.route('/')
def index():
    return 'Index Page'


# `route()` decorator is used to bind a function to a URL
@app.route('/hello')
def hello():
    return 'Happy Vimming!'


def main():
    # debug=True enable the server reload itself on code changes
    # same as `app.debug = True`
    app.run(debug=True)

if __name__ == '__main__':
    main()
