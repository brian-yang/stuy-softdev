from flask import Flask, render_template, session, request, redirect, url_for, flash
from utils import authenticate, database, calculate
import json, urllib2

app = Flask(__name__)

# ===========================================
# MAIN ROUTE
# ===========================================

#have: design doc changes - simple text file
#readme, names, demo link to youtube video, descripion of website, usage instructions
#  -bug info
#  -api keys file if using, email (pm)

@app.route("/", methods = ['GET', 'POST'])
def default():
  if "username" in session:
    usertype = database.getUserType(session["username"])
    if usertype == 0:
      classlist = database.getEnrolledClasses(session["username"])
    elif usertype == 1:
      classlist = database.getAllClasses(session["username"])

    todos = database.getAllTodos(session["username"])

    return render_template("home.html", class_list = classlist, user_type = usertype, todos = todos)
  else:
    return render_template("home.html")

# ===========================================
# ASSIGNMENT/CLASS ROUTES
# ===========================================

@app.route("/assignment/", methods=["POST"])
def assignment():
  d = {}

  #print request.form["grade"]
  print session["username"]
  print request.form["assignment"]
  print session["username"]
  if "username" in session:
    taskid = request.form["assignment"]
    usertype = database.getUserType(session["username"])
    tsubs = database.getAllSubmissionsTeacher(taskid);

    if "grade" in request.form:
      print "setting grade"
      subid = database.getSubmissionData(request.form["student_name"], taskid)[1]
      database.setGrade(subid, request.form["grade"])

    for array in tsubs:
      d[array[1]] = array[3]
    if usertype == 0:
      issub = database.checkSubmission(session["username"], taskid)
      entry = database.getSubmissionData(session["username"], taskid)
      print entry
      print "0request.form[\"class\"]: " + str(request.form["class"])
      if issub:
        subid = database.getSubmissionData(session["username"], taskid)[1]
        return render_template('assignment.html', task_id = taskid, user_type= database.getUserType(session["username"]), issub = issub, entry = entry, class_name = request.form["class"], grade = database.getGrade(subid))
      else:
        return render_template('assignment.html', task_id = taskid, user_type= database.getUserType(session["username"]), issub = issub, entry = entry, class_name = request.form["class"])

    else:
      print "1request.form[\"class\"]: " + str(request.form["class"])
      return render_template('assignment.html', sub = d, class_name = request.form["class"], task_id = taskid)

@app.route("/class/", methods = ['GET','POST'])
def class_html():
  if "username" in session:
    if "description" in request.form and "class" in request.form:
      database.createTask(session["username"], int(database.getClassID(request.form["class"])), request.form["description"])

    if "submission" in request.form:
      database.createSubmission(session["username"], int(request.form["task_id"]), request.form["submission"])
      msg = "Your submission has been stored."
      if "username" in session:
        usertype = database.getUserType(session["username"])
        if usertype == 0:
          classlist = database.getEnrolledClasses(session["username"])
        elif usertype == 1:
          classlist = database.getAllClasses(session["username"])

        return render_template("home.html", class_list = classlist, user_type = usertype, msg = msg)

    if "class" in request.form:
      print "class in request.form case active: " + str(request.form["class"])
      print session["username"]
      print str(database.getAllTasks(database.getClassID(request.form["class"])))
      return render_template('class.html', user_type = database.getUserType(session["username"]), class_name = request.form["class"], tasks = database.getAllTasks(database.getClassID(request.form["class"])))

  return redirect(url_for("default"))

@app.route("/addclass/", methods = ['POST'])
def add_class():
  if "username" in session:
    if "title" in request.form and "code" in request.form:
      if not database.createClass(session["username"], request.form["title"], request.form["code"]):
        flash("A class with that code has already been created either by you or another user.")
  return redirect(url_for("default"))

@app.route("/joinclass/", methods = ['POST'])
def join_class():
  if "username" in session:
    if "code" in request.form:
      if not database.addStudent(request.form["code"], session["username"]):
        flash("Could not find a class with that class code. You may have also already joined the class.")
      #print database.getAllClasses(session["username"])
  return redirect(url_for("default"))

# ===========================================
# AUTHENTICATION ROUTES
# ===========================================

def isLoggedIn():
  if "username" in session:
    if authenticate.isRegistered(session["username"]):
      return True
    session.pop("username")

  return False

#@app.route('/login/', methods = ['POST'])
def login():
  print "login"
  if 'username' in request.form and 'password' in request.form:
    username = request.form['username']
    password = request.form['password']

    if authenticate.authUser(username, authenticate.hash(password)):
      session['username'] = username
      return redirect(url_for('default'))
    else:
      flash('You either have an incorrect username or password, or you did not register!')
  else:
    flash('Please fill out all fields!')
  return render_template('authenticate.html')

#@app.route('/register/', methods = ['POST'])
def register():
  print "register"
  if ('username' in request.form and 'password' in request.form and request.form['password'] != ''):
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm_password']
    occupation = request.form['type']
    if not authenticate.isRegistered(username):
      if password == confirm:
        authenticate.addUser(username, authenticate.hash(password), occupation)
        session['username'] = username
        return redirect(url_for('default'))
      else:
        flash('Passwords must match!')
    else:
      flash('Username already in use!')
  else:
    flash('Please fill out all fields!')
  return render_template('authenticate.html')

#combine register and login into one auth function bc otherwise auth really has no use
#also if you try to manually change the link to localhost:5000/login/ or register you will get an error if you dont combine
@app.route('/auth/', methods = ['GET', 'POST'])
def auth():
  if isLoggedIn():
    flash('Already logged in!')
    return redirect(url_for('default'))
  if (request.method == 'POST'):
    if (request.form['button'] == 'register'):
      return register()
      #return redirect(url_for('default'))
    if (request.form['button'] == 'login'):
      return login()
      #return redirect(url_for('default'))
  return render_template('authenticate.html')

@app.route("/logout/")
def logout():
  if isLoggedIn():
    session.pop("username")
  return redirect(url_for("default"))

@app.route("/profile/")
def profile():
  if isLoggedIn():
    return render_template("profile.html")

  else:
    flash("to access this feature, please log in or register!")
    return render_template("home.html")

@app.route("/changepass/", methods = ["POST"])
def changepass():
  if request.form["oldpass"] and request.form["newpass"]:
    username = session['username']
    curPass = request.form['oldpass']
    newPass = request.form['newpass']
    confirmPass = request.form['confirmpass']
    if authenticate.authUser(username, authenticate.hash(curPass)):
	  if newPass == confirmPass:
	    userID = authenticate.getIDOfUser(username)
	    authenticate.changePassword(userID, authenticate.hash(newPass))
	    flash('Password changed successfully!')
	  else:
	    flash('Passwords must match!')
    else:
	  flash('Incorrect password!')
  else:
    flash('Please fill out all fields!')
  return render_template('profile.html')

# ===========================================
# MISCELLANEOUS ROUTES
# ===========================================
@app.route("/calculator/", methods = ['GET', 'POST'])
def calculator():
  if "username" in session:
    print request.form
    if "input" in request.form:
      #print calculate.calculate(request.form["input"])
      res = calculate.calculate(request.form["input"])
      if "answer" in res:
        res = "Could not calculate. Please enter your input again."

      return render_template("calculator.html", result = res)

    return render_template("calculator.html")
  return redirect(url_for("default"))

@app.route("/todoadd/", methods= ['POST'])
def add_todo():
  if "username" in session:
    if "text" in request.json:
      created = database.createTodo(session["username"], request.json["text"])
      print created
  return json.dumps({'success':True, "text": request.json["text"], "created": created})

@app.route("/todocomplete/", methods= ['POST'])
def complete_todo():
  if "username" in session:
    if "text" in request.json:
      database.finishTodo(session["username"], request.json["text"])
  return json.dumps({'success':True})


# ===========================================
# TEST ROUTE
# ===========================================

@app.route("/test/") #test path to be removed before publishing
def tester():
  #database.createClass('e','new class', '0')
  #database.addStudent(2, 'w')
  database.setGrade(1, 50)
  return render_template('test.html', test = database.getSubmissionData('w', 1))

if __name__ == "__main__":
  app.debug = True
  app.config.from_object("config")
  app.secret_key = app.config["SECRET_KEY"]
  app.run()
