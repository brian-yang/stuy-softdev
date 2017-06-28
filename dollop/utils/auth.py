import hashlib
import sqlite3

def register(user, password):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    salt = get_salt()

    check_user = "SELECT * FROM users WHERE user=?"
    entry = c.execute(check_user, (user,)).fetchone()
    if entry is None:
        register_user = "INSERT INTO users (user, password, story_ids) VALUES (?, ?, NULL)"
        c.execute(register_user, (user, hashlib.sha512(salt + password).hexdigest()))
        success = True
    else:
        success = False

    c.close()
    db.commit()
    db.close()

    return success

def login(user, password):
    f = "data/storyteller.db"
    db = sqlite3.connect(f)
    c = db.cursor()

    salt = get_salt()

    check_user = "SELECT * FROM users WHERE user=?"
    entry = c.execute(check_user, (user,)).fetchone()

    c.close()
    db.commit()
    db.close()

    if entry is None:
        return False
    elif hashlib.sha512(salt + password).hexdigest() != entry[1]:
        return False
    else:
        return True

def get_salt():
    with open("data/salt.txt", 'r') as f:
        return f.readline()
