from flask import Flask,request
import random

app = Flask(__name__)

@app.route("/",methods=["GET"])
def addition():
    op = request.args.get("op")
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if op == "add":
        return {"result":a+b}
    elif op == "sub":
        return {"result":a-b}
    elif op == "div":
        return {"result":a/b}
    elif op == "mul":
        return {"result":a*b}
    else:
        return {"result":"incorrect op"}

@app.route("/signin",methods=["GET"])
def sign_in():
    fname = request.args.get("firstname")
    lname = request.args.get("lastname")
    gmailid = request.args.get("gmailid")

    passwa=random.randint(100000,999999)

    return {"firstname":fname,"lastname":lname,"gmailid":gmailid,"passward":passwa}

@app.route("/health")
def health_check():
    return {"message":"app is ok"}

if __name__ == "__main__":
    app.run(port=8080)