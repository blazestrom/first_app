import random


class Functions:

    def calculator(self,op,a,b):
        if op == "add":
            return a+b
        elif op == "sub":
            return a-b
        elif op == "div":
            return a/b
        elif op == "mul":
            return a*b
        elif op == "sqrt":
            return a*a
        else:
            return "incorrect op"

    def get_user_password(self,lname, fname, email):
        passwa=random.randint(100000,999999)
        return {"firstname":fname,"lastname":lname,"gmailid":email,"passward":passwa}