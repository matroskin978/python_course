# https://docs.python.org/3/library/sqlite3.html
# https://sqlitestudio.pl/

import sqlite3

db = sqlite3.connect('test.db')
cursor = db.cursor()

try:
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    ''')
except sqlite3.OperationalError:
    pass

print('OK')

db.close()
