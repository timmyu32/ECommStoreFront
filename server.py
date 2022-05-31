from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify



import json

import flask
from flask import Flask, Response, request, render_template, redirect, url_for
from flask import jsonify
from flaskext.mysql import MySQL
import flask_login
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'super secret string' 

login_manager = flask_login.LoginManager()
login_manager.init_app(app)



#begin code used for login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)




if __name__ == "__main__":
	#this is invoked when in the shell  you run
	#$ python app.py
	app.run(port=8000, debug=True)