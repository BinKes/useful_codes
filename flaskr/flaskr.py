#import sqlite3
from profile import Profile
from db import app, db, session_scope
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash

#app = Flask(__name__)

@app.route('/')
def index():
    profiles = []
    #with session_scope() as session:
    #    profiles = session.query(Profile).filter(Profile.userId<=3).all()
        #print(profile[0].userInfo)
    return render_template('index.html', profiles=profiles)

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)