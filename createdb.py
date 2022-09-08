import sqlite3

connection = sqlite3.connect('numbers.db')
cursor = connection.cursor()

create_table = '''
    CREATE TABLE numbers (
        id INTEGER PRIMARY KEY,
        number INTEGER,
        date_created DATETIME
    )
'''

cursor.execute(create_table)

connection.commit()
connection.close()
