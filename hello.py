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
from nltk.corpus import stopwords
# from nltk import tokenize
from nltk import stem

from pymongo import Connection
from pymongo.errors import ConnectionFailure
import os
from urlparse import urlsplit

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


class NLTK:
    def __init__(self):
        self.stopwords = stopwords.words('english')
        self._lancaster = stem.LancasterStemmer()
        self._porter = stem.PorterStemmer()
        self._lemmatizer = stem.WordNetLemmatizer()

    def lancaster_stemmer(self, word):
        return self._lancaster.stem(word)

    def porter_stemmer(self, word):
        return self._porter.stem(word)

    def lemmatizer(self, word):
        return self._lemmatizer.lemmatize(word)

n = NLTK()


@app.route('/nltk/stopwords')
def show_stopwords():
    return str(n.stopwords)


@app.route('/nltk/stemmer')
def show_stem():
    word = request.args.get('word', '')
    lancaster_stem = n.lancaster_stemmer(word)
    porter_stem = n.porter_stemmer(word)
    return render_template('stemmer.html',
                           word=word,
                           lancaster_stem=lancaster_stem,
                           porter_stem=porter_stem,)


@app.route('/send_word_stem', methods=['POST'])
def send_word_stem():
    # Get values with `request.form['name']`
    word = request.form['message']
    return redirect(url_for('show_stem', word=word))


#========================================
# MongoDB
def connect2mongodb(db):
    MONGO_URL = os.environ.get('MONGOHQ_URL')
    try:
        if MONGO_URL:
            c = Connection(host=MONGO_URL, port=27017)
            parsed = urlsplit(MONGO_URL)
            db_name = parsed.path[1:]

            # Get your DB
            return c[db_name]
        else:
            c = Connection(host='localhost', port=27017)
        print('Connected successfully')
    except ConnectionFailure, e:
        print(e)
    return c[db]


def searchMongo(dbh, searchword, field):
    # db = connect2mongodb('mydict')
    return dbh.words.find_one({field: searchword}, {'alc_etm.unum': 1})


@app.route('/mongodb')
def mongodb():
    db = connect2mongodb('mydict')
    aio_url_format = 'http://home.alc.co.jp/db/owa/etm_sch?unum={unum}&stg=2'
    word_link = '<a href="{url}" target="_blank">{word}</a>'
    word = request.args.get('word', '')
    word_db = (searchMongo(db, word, 'lemma') or
               searchMongo(db, n.lemmatizer(word), 'lemma') or
               searchMongo(db, n.lancaster_stemmer(word), 'stem') or
               searchMongo(db, n.porter_stemmer(word), 'stem'))
    if word_db:
        word_url = aio_url_format.format(unum=word_db['alc_etm']['unum'])
        return word_link.format(url=word_url, word=word)
    else:
        return 'Not found'


def main():
    # app.run(debug=True) enable the server reload itself on code changes
    # same as `app.debug = True`
    # app.debug = True
    app.run()

if __name__ == '__main__':
    main()
