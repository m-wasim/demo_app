import flask
from flask import Flask,request

printApp=Flask(__name__)



@printApp.route('/home',methods=['GET'])
def printStatus():
    return "This is working.."

printApp.run('localhost',5000)