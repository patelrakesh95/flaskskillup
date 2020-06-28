from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template("bmicalc.html")

@app.route("/calc",methods=["POST"])
def calc():
    # Weight in KG
    weight = request.form.get("weight")
    # Height in cms
    height = request.form.get("height")
    if height != None:
        height = int(height)/100
    if height !=None and weight != None:
        bmi = float(weight)/(height*height)
        bmi = round(bmi,2)
    return render_template("bmicalc.html",bmi=bmi)
