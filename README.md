Learning Flask
-----

### Introduction
- [Welcome | Flask (A Python Microframework)](http://flask.pocoo.org/)
- PDF: [http://flask.pocoo.org/docs/flask-docs.pdf](http://flask.pocoo.org/docs/flask-docs.pdf)
- GitHub: [mitsuhiko/flask](https://github.com/mitsuhiko/flask)

It seems Flask support Python3, but it recommend to use Python 2.7 instead.


### External Libraries
1. WSGI: Werkzeug [Welcome | Werkzeug (The Python WSGI Utility Library)](http://werkzeug.pocoo.org/)
2. Template Engine: Jinja2 [Welcome | Jinja2 (The Python Template Engine)](http://jinja.pocoo.org/)

### virtualenv
#### Install
```
sudo pip install virtualenv
virtualenv venv
```

#### Activate
```
source venv/bin/activate
pip install Flask
```

#### Deactivate
```
deactivate
```

### Generate requirements & Install requirements
```
pip freeze > requirements.txt
pip install -r requirements.txt
```
