from utils import occupations as occ
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Please navigate to /occupations!"

@app.route("/occupations")
def occupationTable():
    occupations = occ.listOccupation()
    randomOccupation = occ.findOccupation()
    return render_template("main.html", jobList = occupations, aJob = randomOccupation)

if __name__ == '__main__':
    app.run()
