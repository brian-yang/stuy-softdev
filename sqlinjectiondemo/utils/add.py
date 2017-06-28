import sqlite3
import random

def create_table():
    db = sqlite3.connect('../data/users.db')
    c = db.cursor()

    create_users = "CREATE TABLE IF NOT EXISTS users (username STRING NOT NULL, pin INTEGER NOT NULL, balance INTEGER NOT NULL);"
    c.execute(create_users)

    c.close()
    db.commit()
    db.close()

def add_user_data(username, pin, balance):
    db = sqlite3.connect('../data/users.db')
    c = db.cursor()

    query = 'INSERT INTO users (username, pin, balance) VALUES(?, ?, ?)'
    c.execute(query, (username, pin, balance))

    c.close()
    db.commit()
    db.close()
