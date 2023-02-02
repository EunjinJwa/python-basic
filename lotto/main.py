from flask import Flask, render_template, request, redirect, send_file
from lotto_number import gen_lucky_numbers

app = Flask("luckyNumber")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate")
def gen_result():
    drw_no = int(request.args.get('drwNo'))
    print(drw_no)
    results = gen_lucky_numbers(drw_no, 5)
    
    return render_template("home.html", results=results)

app.run()
