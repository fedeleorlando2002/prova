from flask import Flask
 
app = Flask("testiera")
 
@app.route("/pulito")
def pulito():
    return "pulito"
 
@app.route("/sporco")
def sporco():
    return "sporco"
 
@app.route("/mucato")
def mucato():
    return "mucato"
 
if __name__ == '__main__':
    app.run()