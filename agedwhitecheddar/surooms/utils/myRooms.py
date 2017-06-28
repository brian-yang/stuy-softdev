import sqlite3
import time
import datetime
import os

DIR = os.path.dirname(__file__)
DIR += '/'
f = DIR + "../data/data.db"

def getRoomsNow(club):
    global f
    db = sqlite3.connect(f)
    og = db.cursor()

    request = "SELECT * from rooms WHERE club = ?"
    info = og.execute(request, (club,))
    li = []

    d = time.strftime("%d/%m/%Y").split("/")
    for rooms in info:
        # print rooms
        # print datetime.date(int(d[2]), int(d[1]), int(d[0]))
        if datetime.date(int(d[2]), int(d[1]), int(d[0])) <= datetime.date(rooms[4], rooms[2], rooms[3]):
            li.append([rooms[0], rooms[1], rooms[2], rooms[3], rooms[4]])

    og.close()
    db.commit()
    db.close()

    # print "LI: " + str(li)

    return li


def getPreviousRooms(club):
    global f
    db = sqlite3.connect(f)
    og = db.cursor()

    request = "SELECT * from rooms WHERE club = ?"
    info = og.execute(request, (club,))
    li = []

    d = time.strftime("%d/%m/%Y").split("/")

    for rooms in info:
        if datetime.date(int(d[2]), int(d[1]), int(d[0])) > datetime.date(rooms[4], rooms[2], rooms[3]):
            li.append([rooms[0], rooms[1], rooms[2], rooms[3], rooms[4]])

    og.close()
    db.commit()
    db.close()
    return li

def getBlockedRooms():
    return getRoomsNow("Not Available")
