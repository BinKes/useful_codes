#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import request
from flask import Flask, url_for
from flask import request
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next='/'))
    print (url_for('profile', username='John Doe'))
    print(url_for('static', filename='style.css'))

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'    
