from flask import Flask, render_template, request, session, redirect, url_for, Response
from utils import get

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def main():
    return render_template("index.html")

@app.route("/practice", methods = ['GET', 'POST'])
def practice():
    super_secret = False
    if "username" in request.form and request.method == 'POST':
        user = request.form["username"]
        balance = get.get_user_data(request.form["username"])

        if user.strip() == "monty":
            user = "Like we were stupid enough to let you hack us that easily. You want the Holy Grail? Maybe write some SeQueLs."
            balance = -10000000

        return render_template("practice.html", super_secret = super_secret, balance = balance, user = user)

    if "pin" in request.form and request.method == 'POST':
        pin = request.form["pin"]
        if pin == "911":
            super_secret = True
        return render_template("practice.html", super_secret = super_secret)

    return render_template("practice.html", super_secret = super_secret)

if __name__ == '__main__':
    app.debug = True
    app.config.from_object('config')
    app.secret_key = app.config['SECRET_KEY']
    app.run()
