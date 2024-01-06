from flask import Flask
 
app = Flask("test")
 
@app.route("/")
def hello():
    return "ciao"
 

    