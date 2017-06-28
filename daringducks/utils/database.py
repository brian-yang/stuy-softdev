import sqlite3
#from utils import authenticate

def createDB():
  global c
  c.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username TEXT, password TEXT, enrolled_classes TEXT, account_type INTEGER);')
  c.execute('CREATE TABLE IF NOT EXISTS tasks (task_id INTEGER PRIMARY KEY, user_id INTEGER, class_id INTEGER, data TEXT);')
  c.execute('CREATE TABLE IF NOT EXISTS submissions (submission_id INTEGER PRIMARY KEY, user_id INTEGER, task_id INTEGER, data TEXT, grade INTEGER);')
  c.execute('CREATE TABLE IF NOT EXISTS classes (class_id INTEGER PRIMARY KEY, user_id INTEGER, class_name TEXT, class_code TEXT, enrolled_users TEXT);')
  c.execute('CREATE TABLE IF NOT EXISTS todos (todo_id INTEGER PRIMARY KEY, user_id INTEGER, data TEXT);')


def initializeDB():
  global c, db
  file = 'data/database.db'
  db = sqlite3.connect(file)
  c = db.cursor()
  createDB()
  return c

def closeDB():
  global db
  db.commit()
  db.close()

#------------------------ Class Operations ---------------------
#TODO
def createClass(username, class_name, class_code): #creates a new class
  user_id = getIDOfUser(username);
  class_name = class_name.strip()
  class_code = class_code.strip()

  initializeDB()

  c.execute("SELECT class_name, class_code FROM classes")
  results = c.fetchall()
  for result in results:
    if class_name == result[0] or class_code == result[1]:
      closeDB()
      return False

  c.execute('INSERT INTO classes (user_id, class_name, class_code) VALUES(?, ?, ?);' , (user_id, class_name, class_code))

  closeDB()

  return True

def getAllClasses(username): #returns classes a teacher has created
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('SELECT class_id, class_name, class_code FROM classes WHERE (user_id = ?)', (user_id,))
  out = c.fetchall()
  closeDB()
  classes = []
  if out:
    for i in range(len(out)):
       classes.append(str(out[i][1])) # class_name
    return classes
  else:
    return ''

def addStudent(class_code, username): #adds student to class
  user_id = getIDOfUser(username)
  class_code = class_code.strip()

  initializeDB()
  c.execute('SELECT enrolled_users FROM classes WHERE (class_code = ?);', (class_code,))
  enrolled = c.fetchone()

  success = False

  print enrolled

  # check if class exists
  if enrolled != None:
    # get list of students in class
    enrolled = enrolled[0]
    if enrolled == None:
      enrolled = ''
    # print "Enrolled users:" + str(enrolled.split("|"))

    # check if user is already in class
    enrolled_list = enrolled.split("|")
    enrolled_list = [student.encode('utf-8') for student in enrolled_list]
    if str(user_id) not in enrolled_list:
      enrolled += str(user_id) + "|"
      c.execute('UPDATE classes SET enrolled_users = ? WHERE class_code = ?', (str(enrolled), str(class_code)))
      success = True
    else:
      success = False

  closeDB()

  return success

def getEnrolledStudents(class_id): # returns comma-separated list of enrolled students
  initializeDB()
  c.execute('SELECT enrolled_users FROM classes WHERE(class_id = ?);' , (class_id,))
  enrolled = c.fetchall()
  closeDB()
  enrolled = str(enrolled[0][0])
  return enrolled

def getEnrolledClasses(username): #returns the classes a student is enrolled in, similar to getAllClasses()
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('SELECT Count(*) FROM classes') #number of classes in table
  m  = c.fetchall()[0][0]
  print "max: " + str(m)
  classes = []
  #iterate once, check all enrolled_users arrays, add class data to classes[] if user enrolled
  while (m > 0):
    c.execute('SELECT class_id, class_name, enrolled_users FROM classes WHERE(class_id = ?);', (m,))
    out = c.fetchall()
    print "current out: " + str(out)
    m -= 1

    if (out[0][2] != None):
      #check for user id, add class name to list
      enrolled = out[0][2]
      users = enrolled.split("|")
      print "enrolled: " + str(enrolled)
      print "users: " + str(users)
      print "user_id: " + str(user_id)
      for curr in users:
        if (str(user_id) == str(curr)):
          classes.append(str(out[0][1]))
    m -= 1
  closeDB()
  return classes

def removeClass(class_id): #removes class
  initializeDB()
  c.execute('DELETE FROM classes WHERE class_id = ?;' , (class_id,))
  closeDB()

#------------------------ Todo Operations ---------------------

def createTodo(username, description): #done: 0
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('SELECT * FROM todos WHERE user_id = ? AND data = ?',(user_id, description.strip()))
  result = c.fetchone()
  if result != None:
    closeDB()
    return False

  c.execute('INSERT INTO todos (user_id, data) VALUES(?, ?);' , (user_id, description.strip()))
  closeDB()

  return True

def finishTodo(username, description):
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('DELETE FROM todos WHERE user_id = ? AND data = ?;' , (user_id, description))
  closeDB()

def getAllTodos(username): #split into two methods?
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('SELECT data FROM todos WHERE(user_id = ?);', (user_id,))
  out = c.fetchall()
  closeDB()
  todos = []
  if out:
    for i in range(len(out)):
      todos.append(str(out[i][0])) #data, done, todo_id
    return todos
  else:
    return ''

#------------------------ Submission Operations ----------------

def createSubmission(username, task_id, data):
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('INSERT INTO submissions (user_id, task_id, data) VALUES(?, ?, ?);' , (user_id, task_id, data))
  closeDB()
  return


def getGrade(submission_id):
  initializeDB()
  c.execute('SELECT grade FROM submissions WHERE submission_id = ?;' , (submission_id,))
  out = c.fetchone()
  print "getGrade out: " + str(out)
  closeDB()
  if out == None:
    return ''
  else:
    return out[0]

def setGrade(submission_id, grade):
  initializeDB()
  c.execute('UPDATE submissions SET grade = ? WHERE submission_id = ?', (grade, submission_id))
  closeDB()
  return

def checkSubmission(username, task_id):
  user_id = getIDOfUser(username)
  initializeDB()
  c.execute("SELECT * FROM submissions WHERE user_id = ? AND task_id = ?", (user_id, task_id))

  result = c.fetchone()

  closeDB()

  hasSubmitted = result != None
  return hasSubmitted

def getAllSubmissionsTeacher(task_id):
  initializeDB()
  c.execute("SELECT * FROM submissions WHERE task_id = ?", (task_id,))
  result = c.fetchall()
  closeDB()
  print 'result getAllSubmissionsTeacher(): ' + str(result)
  if result == None:
    return ''
  else:
    for i in range(len(result)):
      print 'current[1]: ' + str(result[i][1])
      listCurrent = list(result[i])
      result[i] = listCurrent
      result[i][1] = str(getUserOfID(result[i][1]))
      result[i][3] = str(result[i][3])
      print 'current[1]: ' + str(result[i][1])
    return result

def getSubmissionData(username, task_id):
  user_id = getIDOfUser(username)
  initializeDB()
  c.execute("SELECT data, submission_id FROM submissions WHERE user_id = ? AND task_id = ?", (user_id, task_id))

  result = c.fetchone()
  print "getSubmissionData(): " + str(result)
  closeDB()
  if result == None:
    return ''
  else:
    result = list(result)
    result[0] = str(result[0])
    return result
#------------------------ Task Operations ----------------

def createTask(username, class_id, data):
  user_id = getIDOfUser(username);
  initializeDB()
  c.execute('INSERT INTO tasks (user_id, class_id, data) VALUES(?, ?, ?);' , (user_id, class_id, data))
  closeDB()
  return

def getAllTasks(class_id): #in progress, not tested
  initializeDB()
  c.execute('SELECT task_id, data FROM tasks WHERE class_id=?', (class_id,))
  results = c.fetchall()

  task_dict = {}

  for result in results:
    task_dict[result[0]] = result[1]

  closeDB()

  return task_dict

#------------------------ Other Operations ---------------------

def getIDOfUser(username):
  initializeDB()
  c.execute('SELECT user_id FROM users WHERE (username = ?);', (username,))
  out = c.fetchall()
  closeDB()

  if out:
    return out[0][0]
  else:
    return -1

def getUserOfID(user_id):
  initializeDB()
  c.execute('SELECT username FROM users WHERE (user_id = ?);', (user_id,))
  out = c.fetchall()
  closeDB()

  if out:
    return out[0][0]
  else:
    return -1

def getClassID(class_name):
  initializeDB()
  c.execute('SELECT class_id FROM classes WHERE (class_name = ?);', (class_name,))
  result = c.fetchone()
  closeDB()

  if result == None:
    return ''
  else:
    return result[0]

def getUserType(username):
  initializeDB()

  c.execute("SELECT account_type FROM users WHERE username = ?", (username,))
  result = c.fetchone()

  closeDB()

  if result == None:
    print "what"
    return 0
  else:
    return result[0]
