from flask import Flask, render_template

app = Flask("jobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="kassy")

app.run()

