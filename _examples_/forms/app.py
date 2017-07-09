from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    print app
    print request.headers
    return render_template("forms.html")

@app.route("/authenticate/", methods = ['POST'])
def auth():
    #print request.headers
    print request.form
    print request.form['test']
    return "OK"

if __name__ == '__main__':
    app.debug = True
    app.run()
