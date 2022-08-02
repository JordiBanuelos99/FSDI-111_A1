from flask import Flask # we imported Flask class from flask module

app = Flask(__name__) # app is an instance

@app.route("/") # this is a route
def index(): # our view function
    return "<h1>Hello world</h1>" # return string

@app.route("/about")
def about():
    me={
        "first_name:":"Jordi",
        "second_name":"Bañuelos"
    }
    return me