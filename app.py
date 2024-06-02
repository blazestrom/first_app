
from functions import Funtions
from flask import Flask,request



app = Flask(__name__)

@app.route("/",methods=["GET"])
def addition():
    op = request.args.get("op")
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return {"result":Funtions.calculator(op,a,b)}


@app.route("/signin",methods=["GET"])
def sign_in():
    fname = request.args.get("firstname")
    lname = request.args.get("lastname")
    gmailid = request.args.get("gmailid")
    return Funtions.get_user_password(fname,lname,gmailid)

@app.route("/health")
def health_check():
    return {"message":"app is ok"}

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return {"messsage":"Hello world, how are you"}



if __name__ == "__main__":
    app.run(port=8080)