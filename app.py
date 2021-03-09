from flask import Flask

app = Flask("myapp")

@app.route("/")
def my_home():
    print("Welcome to my home")
    return "home"