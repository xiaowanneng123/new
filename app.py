from flask import Flask,render_template,request
import google.generativeai as palm

palm.configure(api_key="AIzaSyBOvs8iOUGUsCL43p6hOIqQzVzNnsd9zZI")
model = {"model":"models/chat-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    r = request.form.get("q")
    return(render_template("main.html",r=r))

@app.route("/genAI",methods=["GET","POST"])
def genAI():
    q = request.form.get("q")
    r = palm.chat(**model,messages=q)
    return(render_template("genAI.html",r=r.last))

@app.route("/DApp",methods=["GET","POST"])
def DApp():
    return(render_template("DApp.html"))

if __name__ == "__main__":
    app.run()
