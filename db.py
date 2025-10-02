import sqlite3

conn = sqlite3.connect('fashion.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    bought INTEGER,
    sold INTEGER
)
''')

# Sample data
items = [
    ('Denim Jacket', 49.99, 100, 60),
    ('Floral Dress', 39.99, 80, 45),
    ('Sneakers', 59.99, 120, 90),
    ('Leather Bag', 89.99, 50, 20)
]

cursor.executemany('INSERT INTO products (name, price, bought, sold) VALUES (?, ?, ?, ?)', items)
conn.commit()
conn.close()
