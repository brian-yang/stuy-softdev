import sqlite3
import hashlib
from utils import database

def createDB():
  database.createDB()

def initializeDB():
  global c
  c = database.initializeDB()

def closeDB():
  database.closeDB()

def addUser(username, passhash, account_type):
  initializeDB()
  print "addUser" + str(account_type)
  c.execute('INSERT INTO users (username, password, account_type) VALUES(?, ?, ?);' , (username, passhash, int(str(account_type))))
  closeDB()

def changePassword(userID, passhash):
  initializeDB()
  c.execute('UPDATE users SET password = ? WHERE (user_id = ?);' , (passhash, userID))
  closeDB()

def isRegistered(username):
  initializeDB()
  c.execute('SELECT * FROM users WHERE (username = ?);' , (username,))
  out = c.fetchall()
  closeDB()
  return bool(out)

def getAccountType(username): # 0 = student; 1 = teacher
  initializeDB()
  c.execute('SELECT account_type FROM users WHERE (username = ?);' , (username,))
  out = c.fetchall()
  closeDB()
  if out:
    return out[0][0]
  else:
    return -1

def getIDOfUser(username):
  initializeDB()
  c.execute('SELECT user_id FROM users WHERE (username = ?);' , (username,))
  out = c.fetchall()
  closeDB()

  if out:
    return out[0][0]
  else:
    return -1

def hash(s):
  return hashlib.sha256(s).hexdigest()

def authUser(username, passhash):
  initializeDB()
  c.execute('SELECT password FROM users WHERE (username = ?);' , (username,))
  out = c.fetchall()
  closeDB()

  if out:
    return out[0][0] == passhash
  else:
    return False
