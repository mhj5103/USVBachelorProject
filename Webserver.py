from flask import Flask, render_template, redirect
from flask import request
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
    print("The coordinate is '" + xcoord + "." + ycoord)
    return redirect('/submitDestination')

if __name__ == '__main__':
   app.run()