from distutils.log import debug
from posixpath import split
from flask import Flask, render_template, request, send_from_directory
import base64
from github import Github
import requests
from flask import Markup
import gunicorn

import os
from flask import Flask,render_template,request,redirect
import smtplib, ssl
from flask_mail import Mail, Message
import json

#defining flask name
app = Flask(__name__)


#Defining home page(index.html)
@app.route('/')
def home():
    return render_template('index.html')


#Returning output for user data
@app.route('/inputs', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        name = request.form['name']
        names = request.form['names']

        return redirect(f"/restraunt/{name}/{names}")
#getting restraunt data
@app.route('/restraunt/<name>/<names>', methods =["GET", "POST"])
def restraunt(name, names):
   
    api_key='xxxxxxx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url='https://api.yelp.com/v3/businesses/search'
 

    params = {f'term':{name},'location':{names}}
 
    req=requests.get(url, params=params, headers=headers)
    b = json.loads(req.text)
    businesses = b["businesses"]

    for business in businesses:
        w = ("Name:", business["name"])
        z = ("Rating:", business["rating"])
        r = ("Address:", " ".join(business["location"]["display_address"]))
        c = ("Phone:", business["phone"])


    return render_template("data.html",  splits = Markup(f'<b>Name:</b> {w}<br><b>Rating:</b> {z}<br><b>Address:</b> {r}<br><b>Phone</b> {c}<br>')
)
#Running Flask
if __name__ == "__main__":
    app.run(debug=True)