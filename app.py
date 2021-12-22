from flask import Flask,render_template, request
import requests
from os import getcwd,listdir 


app = Flask(__name__)

#home page
@app.route("/")
def index():
  return render_template("index.html")
  
#source code page  
@app.route("/source",methods=['GET','POST'])
def source():
  if request.method == 'POST':
    url = request.form['url']
    own_link = "http://localhost:5000/"
    if url == own_link:
      return render_template("error-page.html")
    #extract source code
    try:
      req = requests.get(url)
      resp = req.text 
      return render_template("source-code.html",resp=resp)
    except:
      pass
  return render_template("index.html")


if __name__=="__main__":
  app.run(debug=True)