from flask import Flask
from flask_httpauth import HTTPBasicAuth

#Basic authentication example

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john1": "hello",
    "susan": "bye"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()
'''
@auth.hash_password
def hash_pw(password):
    return md5(password).hexdigest()

@auth.hash_password
def hash_pw(username, password):
    get_salt(username)
    return hash(password, salt)
'''

if __name__ == '__main__':
    app.run()
