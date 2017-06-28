import sqlite3   # enable control of an sqlite database

f="discobandit.db"

db = sqlite3.connect(f) # open if f exists, otherwise create
c = db.cursor()    # facilitate db ops

#==========================================================
# INSERT YOUR POPULATE CODE IN THIS ZONE
# ...perhaps by beginning with these examples...
#==========================================================
#---------------------------------------------------------
print("Please run db_builder.py if there's an error to create the tables first!")
print("")

q = "SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id;"
sel = c.execute(q)

student_grades = {}

for entry in sel:
    print entry

    student_name = entry[0]
    sid = entry[1]
    grade = entry[2]

    if sid not in student_grades:
        # format is [name, grade, num of courses taken]
        student_grades[sid] = [student_name, grade, 1]
    else:
        # add grade for course and inc num of courses taken
        student_grades[sid][1] += grade
        student_grades[sid][2] += 1

print("")
for sid in range(1, len(student_grades) + 1):
    print("%s's (id %d) average: %.3f" % (student_grades[sid][0], sid, float(student_grades[sid][1]) / student_grades[sid][2]))

c.close()
db.commit()
db.close()
