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

### Deploy to Heroku on Ubuntu

#### 1. Install heroku command-line tools
> `wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh`
> https://toolbelt.heroku.com/

#### 2. Login
```
heroku login
```

#### 3. Create
```
heroku create
```

#### 4. Deploy!
```
heroku keys:add ~/.ssh/id_rsa.pub
git push heroku master
```

#### 5. Specifying a Python Runtime
runtime.txt
```
python-3.3.4
```

## NLTK
```
wget http://nltk.org/nltk3-alpha/nltk-3.0a3.zip
unzip nltk-3.0a3.zip
cd nltk-3.0a3
python setup.py install
pip freeze > requirements.txt
```

requirements.txt
```
nltk -> ./nltk-3.0a3/
```

```
mkdir ./nltk_data
python
import nltk
nltk.download()
# Install to ./nltk_data directory
```

## MongoDB
```
heroku addons:add mongohq
heroku config
-> MONGOHQ_URL => mongodb://heroku:<password>@<hostname>.mongohq.com:<port_number>/<database_name>
```

### Upload local mongodb database to heroku
```
mongodump -h <local_host>:<local_port> -d <local_database_name> -o <dump_db_path>
mongorestore -h <hostname>.mongohq.com:<port_number> -d <database_name> -u heroku -p <password>  <dump_db_path>/<local_database_name>
```

### Sample code on Python3
sample.py
```
import os
from urllib.parse import urlsplit

def connect2mongodb(db):
    MONGO_URL = os.environ.get('MONGOHQ_URL', None)
    if MONGO_URL:
        # For heroku
        c = Connection(host=MONGO_URL, port=27017)
        parsed = urlsplit(MONGO_URL)
        db_name = parsed.path[1:]

        # Get your DB
        return c[db_name]
    else:
        c = Connection(host='localhost', port=27017)
        return c[db]
```

