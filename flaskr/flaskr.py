#import sqlite3
import os
from profile import Profile
from db import app, db, session_scope
from flask import Flask, request, g, redirect, url_for, abort, render_template, flash, session

#app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    AGE=70
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route('/')
def index():
    #profileInfo = []
    with session_scope() as session:
        profiles = session.query(Profile).filter(Profile.userId<=3).all()
        print(profiles[0].userInfo)
        #profiles = [{'name':'abc','age':20},{'name':'dsd','age':30}]
        #for profile in profiles:
        #    profileInfo.append(profile.userInfo)

        return render_template('index.html', profiles=profiles)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    #db = get_db()
    #db.execute('insert into entries (title, text) values (?, ?)',
    #             [request.form['title'], request.form['text']])
    #db.commit()
    #flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello():
    return render_template('hello.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    profiles = []
    if request.method == 'POST':
        with session_scope() as s:
            profiles = s.query(Profile).filter(Profile.name==request.form['name']).all()
        
        if int(request.form['age']) <= app.config['AGE']:
            error = 'Invalid age'
        elif not profiles:
            error = 'Invalid username'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)