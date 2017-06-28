import sqlite3

def get_user_data(username):
    try:
        db = sqlite3.connect('home/softdevsql1/mysite/data/users.db') # should be changed if testing locally
        c = db.cursor()

        query = "SELECT * FROM users WHERE username=%s" % username
        print query
        info = c.execute(query).fetchall()
        print info

        if info is None or info == []:
            info = [0]
        elif len(info) == 1:
            info = info[0]

        c.close()
        db.commit()
        db.close()
    except:
        info = [0]

    return info
