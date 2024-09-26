import sqlite3


def init_db():
    conn = sqlite3.connect(':memory:')  # создание базы данных в оперативной памяти
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')

    return conn


def add_user(conn, name, age):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age, ))
    conn.commit()


def get_user(conn, name):
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM users WHERE name = ?
    ''', (name, ))
    return cur.fetchone()
