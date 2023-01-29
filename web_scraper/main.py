from flask import Flask, render_template, request, redirect, send_file
from extractors.job_extractor import extract_job
from file import save_to_file
from database.db_memory import get, exists_keyword


app = Flask("jobScrapper")

@app.route("/")
def home():
    return render_template("home.html", name="kassy")

@app.route("/search")
def search():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect("/")
    jobs = extract_job(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get('keyword')
    if keyword == None:
        return redirect("/")
    if exists_keyword(keyword) == False:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, get(keyword))
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run()

