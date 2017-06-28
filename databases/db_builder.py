import sqlite3   # enable control of an sqlite database
import csv       # facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

#==========================================================
# INSERT YOUR POPULATE CODE IN THIS ZONE
# ...perhaps by beginning with these examples...
#==========================================================
#---------------------------------------------------------
# returns a dictObject containing the parsed csv
def dictObject(filename):
    fobj = open(filename)
    d = csv.DictReader(fobj)
    return d
#---------------------------------------------------------
# deletes the students table if it already exists
drop = "DROP TABLE if exists students"
c.execute(drop)

q = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
c.execute(q)    #run SQL query

studentDict = dictObject("peeps.csv")
students = []
for entry in studentDict:
    # store each row's values into variables
    name = entry['name']
    age = int(entry['age'])
    id = int(entry['id'])
    # append a tuple (AKA a set) to the list of students
    students.append((name, age, id))

# run INSERT for each tuple in students
c.executemany('INSERT INTO students VALUES (?,?,?)', students) 
#---------------------------------------------------------
# deletes the courses table if it already exists
drop = "DROP TABLE if exists courses"
c.execute(drop)

q = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"
c.execute(q)
# c.execute(q)

coursesDict = dictObject("courses.csv")
courses = []
for entry in coursesDict:
    # store each row's values into variables
    code = entry['code']
    mark = int(entry['mark'])
    id = int(entry['id'])
    # append a tuple (AKA a set) to the list of students
    courses.append((code, mark, id))

# run INSERT for each tuple in students
c.executemany('INSERT INTO courses VALUES (?,?,?)', courses) 
#---------------------------------------------------------
c.close()
#==========================================================
db.commit() # save changes
db.close()  # close database
