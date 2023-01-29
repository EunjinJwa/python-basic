from flask import Flask, render_template, request
from extractors.job_extractor import extract_job


app = Flask("jobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="kassy")

@app.route("/search")
def search():
    keyword = request.args.get('keyword')
    jobs = extract_job(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run()

