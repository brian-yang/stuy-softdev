from flask import Flask, render_template, request, session, redirect, url_for
from utils import credentials

app = Flask(__name__)
app.secret_key = "asdasdasda"

@app.route("/")
def main():
    if "user" in session.keys():
        return render_template("welcome.html", username = session["user"])
    else:
        return redirect(url_for("login"))

@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/logout/")
def logout():
    if "user" in session.keys():
        del session["user"]
        return render_template("logout.html")
    return redirect(url_for("login"))

@app.route("/authenticate/", methods = ['POST'])
def auth():
    if "register" in request.form:
        return render_template("login.html", registered = credentials.register_user(request.form["username"], request.form["password"]))
    elif "login" in request.form:
        message = credentials.login_user(request.form["username"], request.form["password"])
        if "Success" in message:
            session["user"] = request.form["username"]
            return redirect(url_for("main"))
        else:
            return render_template("authenticate.html", logged_in = message)
            
if __name__ == '__main__':
    app.debug = True
    app.run()
