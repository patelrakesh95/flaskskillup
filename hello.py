from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<string:name>")
def name(name):
    name = name.capitalize()
    return f"Hello {name}!"
