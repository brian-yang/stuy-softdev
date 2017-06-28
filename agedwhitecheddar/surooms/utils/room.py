import hashlib
import sqlite3
import os
import time
import collections

DIR = os.path.dirname(__file__)
DIR += '/'
f = DIR + "../data/data.db"

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getMonthName(num):
    return time.strftime('%B', time.struct_time((0, num, 0,)+(0,)*6))

def getInfoMonth(month, year):
    global f
    db = sqlite3.connect(f)
    og = db.cursor()
    # print year
    request="SELECT room, club, month, day from rooms WHERE month = ? and year = ? ORDER BY day;"
    info = og.execute(request, (month, year))
    l = []
    if info is not None:
        for entry in info:
            l.append(entry)

    og.close()
    db.commit()
    db.close()
    return l

def getInfoYear(year):
    l = []
    # print year
    for i in range(1,13):
        l.append(getInfoMonth(i,year))
    dic = collections.OrderedDict()
    for i in range(1,13):
        dic[getMonthName(i)] = l[i-1]
    return dic

def getInfoDate(month,day,year):
    global f
    db = sqlite3.connect(f)
    og = db.cursor()
    request="SELECT room,club from rooms WHERE month = ? and day = ? and year = ?;"
    info = og.execute(request, (month,day, year))
    l = []
    if info is not None:
        for entry in info:
            l.append(entry)

    og.close()
    db.commit()
    db.close()
    print "L: " 
    print l
    return l



def getInfoRangeYear(year1,year2):
    dic = collections.OrderedDict()
    yr1 = int(year1)
    yr2 = int(year2)
    while yr1 - yr2 != 0:
        dic[str(yr1)] = getInfoYear(str(yr1))
        yr1 = yr1 + 1
    dic[year2] = getInfoYear(year2)
    return dic

'''def getInfoRange(start, end):
    info=[]
    startN=int(start[
'''

#gets all the rooms, clubs, for a specific date
#date format: mmddyyyy
def getInfoClub(clubName):
    global f
    db = sqlite3.connect(f)
    og = db.cursor()
    date = (time.strftime("%d%m%Y"))
    request="SELECT * from rooms WHERE day = ? and month = ? and year = ? and clubName = ?;"
    info=og.execute(request, (int(date[2:4]), int(date[:2]), int(date[4:]), clubName))
    l=[]
    for thing in info:
        l.append(thing[0],thing[1],thing[2])

    og.close()
    db.commit()
    db.close()

    return l
