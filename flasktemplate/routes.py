from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/math")
def addition():
    return str(3 + 5)

@app.route("/test")
def test():
    return "Testing."

if __name__ == '__main__':
    app.run()
