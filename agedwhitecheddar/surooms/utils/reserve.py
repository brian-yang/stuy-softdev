import sqlite3
import time
import os
import approve
#date format: mmddyyyy

DIR = os.path.dirname(__file__)
DIR += '/'
f = DIR + "../data/data.db"

def reserve_room(room, date, clubName):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()

    check = "SELECT club FROM rooms WHERE  room = ? AND month = ? and day = ? and year = ?"
    auth = c.execute(check, (room, int(date[0:2]) + 1, int(date[2:4]), int(date[4:]))).fetchone()

    if auth is None:
        add_reservation = "INSERT INTO rooms (room, club, month, day, year) VALUES(?, ?, ?, ?, ?) "
        c.execute(add_reservation, (room, clubName, int(date[0:2]) + 1 , int(date[2:4]), int(date[4:])))

        c.close()
        db.commit()
        db.close()

        return True

    c.close()
    db.commit()
    db.close()
    return False

# can unreserve if the club that reserved the room
def unreserve_room_club(room, date, clubName):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()

    unreserve = "DELETE FROM rooms WHERE room = ? and month = ? and day = ? and year = ?"
    c.execute(unreserve, (room, int(date[0:2]) , int(date[2:4]), int(date[4:])))

    c.close()
    db.commit()
    db.close()

def whatClub(room, date):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()
    print room
    print date

    search = "SELECT club FROM rooms WHERE room = ? and month = ? and day = ? and year = ?"
    info  = c.execute(search, (room, int(date[0:2]) + 1 , int(date[2:4]), int(date[4:]))).fetchall()
    if info != None:
        p = info[0][0]
    else:
        p = []

    c.close()
    db.commit()
    db.close()

    return p

# if room is being blocked, kick out people who already made a reservation
# prevent clubs from reserving room again
def block_room(room, date):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()

    kick_out_reserved = "DELETE FROM rooms WHERE room = ? and month = ? and day = ? and year = ? "
    c.execute(kick_out_reserved, (room, int(date[0:2]) + 1, int(date[2:4]), int(date[4:])))

    block_reservation = "INSERT INTO rooms (room, club, month, day, year) VALUES(?, ?, ?, ?, ?) "
    c.execute(block_reservation, (room, "Not Available", int(date[0:2]) + 1, int(date[2:4]), int(date[4:])))

    c.close()
    db.commit()
    db.close()

def unblock_room(room, date, cor = 0):
    global f
    db = sqlite3.connect(f)
    c = db.cursor()
    d = date.strip().split("-")
    d2 = ""
    for i in d:
        d2 += str(i).zfill(2)
    date = d2
    print "dfsdfsdf"
    print "dfsfgdfsd"
    unreserve = "DELETE FROM rooms WHERE room = ? and month = ? and day = ? and year = ?"
    c.execute(unreserve, (room, int(date[0:2]) + cor , int(date[2:4]), int(date[4:])))

    c.close()
    db.commit()
    db.close()
