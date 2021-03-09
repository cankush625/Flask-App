from flask import Flask, render_template
import subprocess as sp

app = Flask("myapp")

@app.route("/")
def my_home():
    date = sp.getoutput("date /t")
    return render_template("home.html", date=date)