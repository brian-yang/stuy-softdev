from flask import Flask, render_template, session, request, redirect, url_for
from utils import auth, add, get

app = Flask(__name__)

# ===========================================
# MAIN
# ===========================================
@app.route("/")
def main():
    if "user" not in session.keys():
        return render_template("login.html", error= "We see you aren't logged in. Please login, or register for an account, to access the site.")
    else:
        return render_template("main.html", user = session["user"], story = get.get_contributed_stories(session["user"]))

# ===========================================
# LOGIN/LOGOUT
# ===========================================
@app.route("/authenticate/", methods = ["POST"])
def authenticate():
    if request.form['submit'] == 'register':
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.register(request.form['username'], request.form['password']):
            msg = "Successfully registered!"
        else:
            msg = "Failed to register! Username is taken."
        return render_template("login.html", message = msg)

    elif request.form['submit'] == 'login':
        if not request.form['username'] or not request.form['password']:
            msg = "Please enter a username and password."
        elif auth.login(request.form['username'], request.form['password']):
            session["user"] = request.form['username']
            return redirect(url_for("main"))
        else:
            msg = "Failed to login. Username and/or password incorrect."
        return render_template("login.html", message = msg)

@app.route("/logout/")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for("main"))

# ===========================================
# CREATRE, BROWSE, AND UPDATE STORIES
# ===========================================
@app.route("/browse/")
def browse():
    if "user" in session.keys():
        return render_template("browse.html", story = get.get_browse_stories(session["user"]))
    else:
        return redirect(url_for("main"))

@app.route("/new/", methods = ["GET", "POST"])
def create_story():
    if "user" in session.keys():
        if "story" in request.form.keys():
            add.add_new_story(request.form["title"], session["user"], request.form["story"])
            return redirect(url_for("main"))
        else:
            return render_template("create.html")
    else:
        return redirect(url_for("main"))

@app.route("/update/", methods = ["POST"])
def update():
    if 'user' in session.keys():
        if "update" in request.form.keys():
            add.store_updates(session["updating_story_id"], session["user"], request.form["update"])
            session.pop("updating_story_id")
            return redirect(url_for("main"))
        elif "browse" in request.form.keys():
            session["updating_story_id"] = request.form["browse"]
            print get.get_latest_update(request.form["browse"])
            return render_template("update.html", line = get.get_latest_update(request.form["browse"]))
        else:
            return redirect(url_for("browse"))
    else:
        return redirect(url_for("main"))

@app.route("/read/",methods = ["POST"])
def read():
    if 'user' in session.keys():
        if "select_read" in request.form.keys():
            selectedid = request.form["select_read"]
            return render_template("read.html",story=get.get_complete_story(selectedid))
        else:
            return redirect(url_for("main"))
    else:
        return redirect(url_for("main"))

# ===========================================
# ERROR PAGE
# ===========================================
@app.errorhandler(404)
def page_not_found(error):
    return "Error!"

# ===========================================
# RUN
# ===========================================
if __name__ == '__main__':
    app.debug = True
    app.config.from_object('config')
    app.secret_key = app.config['SECRET_KEY']
    app.run()
