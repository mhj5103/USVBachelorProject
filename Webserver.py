from flask import Flask, render_template, redirect
from flask import request
from pysondb import db
a=db.getDb("db.json")
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/index')
def home():
   return render_template('index.html')

@app.route('/submitDestination')
def SubmitDestination():
    return render_template('submitDestination.html')

@app.route('/dataRecieved', methods = ['POST'])
def dataRecieved():
    xcoord = request.form['XCoord']
    ycoord = request.form['YCoord']
    a.update({"name":"XCoord"},{"value":xcoord})
    a.update({"name":"YCoord"},{"value":ycoord})
    print("The coordinate is '" + xcoord + "." + ycoord)
    fo = open("updatedDB.txt", "wb")
    return redirect('/submitDestination')

@app.route('/submitPID')
def SubmitPID():
    return render_template('submitPID.html')

@app.route('/pidDataRecieved', methods = ['POST'])
def piddataRecieved():
    Kp = request.form['Kp']
    Ki = request.form['Ki']
    Kd = request.form['Kd']
    a.update({"name":"Kp"},{"value":Kp})
    a.update({"name":"Ki"},{"value":Ki})
    a.update({"name":"Kd"},{"value":Kd})
    print("The pid controls are '" + Kp + "," + Ki + "," + Kd)
    fo = open("updatedDB.txt", "wb")
    return redirect('/submitPID')

@app.route('/submitPID2')
def SubmitPID2():
    return render_template('submitPID2.html')

@app.route('/pidDataRecieved2', methods = ['POST'])
def piddataRecieved2():
    Kp = request.form['Kp']
    Ki = request.form['Ki']
    Kd = request.form['Kd']
    a.update({"name":"Kp2"},{"value":Kp})
    a.update({"name":"Ki2"},{"value":Ki})
    a.update({"name":"Kd2"},{"value":Kd})
    print("The pid controls are '" + Kp + "," + Ki + "," + Kd)
    fo = open("updatedDB.txt", "wb")
    return redirect('/submitPID2')

@app.route('/submitPID3')
def SubmitPID3():
    return render_template('submitPID3.html')

@app.route('/pidDataRecieved3', methods = ['POST'])
def piddataRecieved3():
    Kp = request.form['Kp']
    Ki = request.form['Ki']
    Kd = request.form['Kd']
    a.update({"name":"Kp3"},{"value":Kp})
    a.update({"name":"Ki3"},{"value":Ki})
    a.update({"name":"Kd3"},{"value":Kd})
    print("The pid controls are '" + Kp + "," + Ki + "," + Kd)
    fo = open("updatedDB.txt", "wb")
    return redirect('/submitPID')

if __name__ == '__main__':
   app.run()