import hashlib
import sqlite3
import os

DIR = os.path.dirname(__file__)
DIR += '/'
f = DIR + "../data/data.db"

def addClub(name, email, advisorName, advisorEmail):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()

    query = "INSERT INTO clubs (name, email, advisor, advisorEmail) VALUES (?, ?, ?, ?)"
    c.execute(query, (name, email, advisorName, advisorEmail))

    c.close()
    db.commit()
    db.close()

def getClub(username):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()

    checkUser = "SELECT * FROM clubs WHERE email = ?"
    c.execute(checkUser, (username,))

    r = c.fetchone()
    c.close()
    db.commit()
    db.close()

    return r

def getAllClubs():
    db = sqlite3.connect(f)
    c = db.cursor()

    q = "SELECT * FROM clubs;"
    c.execute(q)

    r = c.fetchall()
    c.close()
    db.commit()
    db.close()

    return r

def getClubName(username):
    return getClub(username)[0]

def getClubEmail(username):
    return getClub(username)[1]

def getAdvisor(username):
    return getClub(username)[2]

def getAdvisorEmail(username):
    return getClub(username)[3]
