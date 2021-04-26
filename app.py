from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/mypage')
def kotel0():
    return render_template('kotel0.html')

@app.route('/mypage/me')
def kotel1():
    return render_template('kotel1.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def kotel2():
   if request.method == 'GET':
       print("We received GET")
       return render_template("kotel2.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.kotel2)
       return redirect("/")