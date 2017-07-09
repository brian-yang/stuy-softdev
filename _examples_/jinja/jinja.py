from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    l = [1, 2, 3]
    return render_template("main.html", message = "Ok!", fred = l)

if __name__ == '__main__':
    app.debug = True
    app.run()    
