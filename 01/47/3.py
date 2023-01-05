# https://docs.python.org/3/library/sqlite3.html
# https://sqlitestudio.pl/

import sqlite3


def dict_factory(cur, row):
    fields = [column[0] for column in cur.description]
    return {key: value for key, value in zip(fields, row)}


db = sqlite3.connect('../test.db')
# db.row_factory = sqlite3.Row
# db.row_factory = dict_factory
cursor = db.cursor()

# cursor.execute("SELECT * FROM users WHERE email = ?", ('caesar@gmail.com',))
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", ('caesar@gmail.com', 'Наполеон Бонапарт'))
# cursor.execute("SELECT * FROM users WHERE email = :email OR name = :name", {'email': 'caesar@gmail.com', 'name': 'Наполеон Бонапарт'})
# res = cursor.fetchone()
#
# if res:
#     print(res[1])
#     print(res[2])

# cursor.execute("SELECT * FROM users")
# res = cursor.fetchall()
# print(res)
# for item in res:
#     print(f"Name: {item['name']}, Email: {item['email']}")

# users = [
#     ('user 1', 'user1@gmail.com'),
#     ('user 2', 'user2@gmail.com'),
#     ('user 3', 'user3@gmail.com'),
# ]
# cursor.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", users)
# cursor.execute("SELECT * FROM users WHERE email LIKE ?", ('%user%',))
# res = cursor.fetchall()
# print(res)

# cursor.execute("UPDATE users SET name = UPPER(SUBSTR(name, 1, 1)) || SUBSTR(name, 2) WHERE email LIKE ?", ('%user%',))
# db.commit()
# cursor.execute("DELETE FROM users WHERE id > 10")
# db.commit()

db.close()
