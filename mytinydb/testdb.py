from tinydb import TinyDB, where, Query


db = TinyDB('db.json')

User = Query()
db.insert({'int': 1, 'char': 'a', 'name':'John'})
db.insert({'int': 1, 'char': 'b'})
print(db.search(User.name == 'John'))