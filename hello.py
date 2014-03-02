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

from random import choice

''' Import the Flask class.
An Instance of this class will be our WSGI application
'''
from flask import Flask, url_for, request, render_template, redirect

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
    # http://localhost:5000/
    # return 'Index Page'
    return render_template('index.html', title='Learning Flask')


# `route()` decorator is used to bind a function to a URL
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # http://localhost:5000/hello
    # http://localhost:5000/hello/haya14busa
    return render_template('hello.html', name=name)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id, the id is an integer
    # The following converters exists
    # -------------------------------------------------
    # int   | accepts integers
    # float | like `int` but for floating point values
    # path  | like the default but also accepts slashes
    # -------------------------------------------------
    # http://localhost:5000/post/14
    return 'Post {id}'.format(id=post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # http://localhost:5000/login
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'


@app.route('/user')
def show_user_by_parameters():
    # http://localhost:5000/user?user=haya14busa
    user = request.args.get('user', '')
    return user


@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for that user
    # http://localhost:5000/user/haya14busa
    return 'User {username}'.format(username=username)


@app.route('/user/redirect')
def redirect_user_by_parameters():
    # http://localhost:5000/user/redirect?user=haya14busa
    user = request.args.get('user', '')
    return redirect(url_for('hello', name=user))


@app.route('/learn/url_building')
def learn_url_building():
    # with app.test_request_context():
    # http://localhost:5000/learn/url_building
    # url_for() looks for **function** instead of URL
    text = \
        '''
        url_for('index') : {index}<br>
        url_for('login') : {login}<br>
        url_for('login', next='/') : {login_next}<br>
        url_for('show_user_profile', username='haya14busa') : {profile}<br>
        '''.format(index=url_for('index'),
                   login=url_for('login'),
                   login_next=url_for('login', next='/'),
                   profile=url_for('show_user_profile',
                                   username='haya14busa'),)
    return text


@app.route('/static_file')
def static_file():
    return url_for('static', filename='style.css')


@app.route('/random')
def random():
    # http://localhost:5000/random
    return choice([str(i) for i in range(1000)])
    # return choice(list(map((lambda x: str(x)), range(1000))))


# Learn POST by Change Title Sample Application
# http://localhost:5000/post_title
# http://localhost:5000/post_title?title=Happy+Vimming!
# See: http://kuroneko0208.hatenablog.com/entry/2013/11/27/043038
@app.route('/post_title')
def post_title():
    title = request.args.get('title', 'Change Title')
    return render_template('post_title.html', title=title)


@app.route('/send_title', methods=['POST'])
def send_title():
    # Get values with `request.form['name']`
    title = request.form['message']
    return redirect(url_for('post_title', title=title))


def main():
    # debug=True enable the server reload itself on code changes
    # same as `app.debug = True`
    app.run(debug=True)

if __name__ == '__main__':
    main()
