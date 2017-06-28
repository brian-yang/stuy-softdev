import hashlib
import sqlite3
import os
import random
from approve import sendEmail

DIR = os.path.dirname(__file__)
DIR += '/'
f = DIR + "../data/data.db"

def hashp(x):
    h = hashlib.sha256()
    h.update(x)
    return h.hexdigest()

def createAccount(user, password, code):
    global f
    isAdmin = int(code[-1])
    db = sqlite3.connect(f)

    sp = db.cursor()
    insert = "INSERT INTO users VALUES (?, ?, ?)"
    sp.execute(insert, (user, hashp(password), isAdmin))

    sp.close()
    db.commit()
    db.close()

'''
Makes sure that the username and password given are valid.
'''
def checkLogin(usern, pw):
    hashed = hashp(pw)
    global f

    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT usern, pw FROM users WHERE usern = ? and pw = ?"
    t = sp.execute(s, (usern, hashed)).fetchone()

    if t is None:
        sp.close()
        db.commit()
        db.close()

        return False
    else:
        sp.close()
        db.commit()
        db.close()

        return True

def getPass(usern):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT pw FROM users WHERE usern = ?"
    t = sp.execute(s, (usern,)).fetchone()

    sp.close()
    db.commit()
    db.close()

    return t

def changePassword(usern,pw):
    hashed = hashp(pw)

    global f
    db = sqlite3.connect(f)
    sp = db.cursor()
    s = "UPDATE users SET pw = ? WHERE usern = ?"
    sp.execute(s, (hashed,usern))

    sp.close()
    db.commit()
    db.close()

'''
If true is returned, that means that the user
can sign up an account with the given email and code.
'''
def checkRegister(email, code):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    query = "SELECT email, code FROM codes WHERE email = ? AND code = ?"
    t = sp.execute(query, (email, code))

    res = t.fetchone()
    if res is None:
        sp.close()
        db.commit()
        db.close()

        return False

    sp.close()
    db.commit()
    db.close()

    return True

def signup_completed(user):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    admin_level_query = "SELECT isAdmin from users WHERE usern = ?"
    r = sp.execute(admin_level_query, (user,)).fetchone()

    signed_up_query = "SELECT email from clubs WHERE email = ?"
    r2 = sp.execute(signed_up_query, (user,)).fetchone()

    signed_up = False
    if r != None: # student signed up
        if int(r[0]) > 0:
            signed_up = True
        if int(r[0]) == 0 and r2 != None: # signed up the club
            signed_up = True

    sp.close()
    db.commit()
    db.close()

    return signed_up

# ================================
# ACCOUNT CODE CREATION
# ================================

'''
To be used by the person in charge of the room reservation
website so that clubs can create accounts.
'''
def storeCode(email, isAdmin):
	if emailUsed(email):
            return "email already approved"
        global f
	db = sqlite3.connect(f)
	sp = db.cursor()
	code = generateCode(isAdmin)
	while codeUsed(code):
		code = generateCode(isAdmin)

	insert = "INSERT INTO codes VALUES (?, ?)"
	sp.execute(insert, (email, code))
	sp.close()
	db.commit()
	db.close()

	sendEmail(email, code)

def generateCode(isAdmin):
    return str(int(random.random()*10000)) + str(isAdmin)

# ================================
# ACCOUNT CODE CHECKING
# ================================
'''
Gets an admin level for a specific user.
'''

def getAdminLevel(email):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    s = "SELECT code FROM codes WHERE email = ?"
    t = sp.execute(s, (email,))

    res = t.fetchall()

    sp.close()
    db.commit()
    db.close()

    return res[0][-1][-1]


'''
Checks if a code was used.
'''
def codeUsed(code):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    request = "SELECT code FROM codes;"
    codes = sp.execute(request).fetchall()

    for usedCode in codes:
        if usedCode[0] == code:
            sp.close()
            db.commit()
            db.close()

            return True

    sp.close()
    db.commit()
    db.close()

    return False

def emailUsed(email):
    global f
    db = sqlite3.connect(f)
    sp = db.cursor()

    request = "SELECT email FROM codes;"
    codes = sp.execute(request).fetchall()

    for usedEmail in codes:
        if usedEmail[0] == email:
            sp.close()
            db.commit()
            db.close()

            return True

    sp.close()
    db.commit()
    db.close()

    return False

def validCred(email,code):
        global f
	db = sqlite3.connect(f)
	sp = db.cursor()
	s = "SELECT email, code FROM codes WHERE email = ? and code = ?"
	t = sp.execute(s, (email, code)).fetchone()
	if t is None:
            sp.close()
            db.commit()
            db.close()

            return False
	else:
            sp.close()
            db.commit()
            db.close()

            return True

def isStudent(code):
	return int(code[-1]) == 0
