# https://docs.python.org/3/library/sqlite3.html
# https://sqlitestudio.pl/

import sqlite3

db = sqlite3.connect('../test.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# cursor.execute("""
# INSERT OR IGNORE INTO users (name, email) VALUES ('Иван Иванов', 'ivanov@gmail.com')
# """)
# cursor.execute("""
# INSERT OR IGNORE INTO users (name, email) VALUES ('John Doe', 'doe@gmail.com')
# """)
# cursor.execute("""
# INSERT OR IGNORE INTO users (name, email) VALUES ('Jack Black', 'black@gmail.com')
# """)

# cursor.executescript("""
# INSERT OR IGNORE INTO users (name, email) VALUES ('Tom Cruise', 'cruise@gmail.com');
# INSERT OR IGNORE INTO users (name, email) VALUES ('Jack Black', 'black@gmail.com');
# INSERT OR IGNORE INTO users (name, email) VALUES ('Юлий Цезарь', 'caesar@gmail.com');
# """)

# users = [
#     ('Спартак', 'spartacus@gmail.com'),
#     ('Наполеон Бонапарт', 'napoleon@gmail.com'),
#     ('Юлий Цезарь', 'caesar@gmail.com'),
#     ('Шерлок Холмс', 'holmes@gmail.com'),
# ]
#
# cursor.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", users)

cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ['John Watson', 'watson@gmail.com'])
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ['Юлий Цезарь', 'caesar@gmail.com'])
cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ('Николь Кидман', 'kidman@gmail.com'))

db.commit()

db.close()
