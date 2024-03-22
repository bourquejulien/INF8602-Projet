#!/bin/env python3

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    print(username, password)

    # conn = psycopg2.connect(database = "datacamp_courses", 
    #                     user = "datacamp", 
    #                     host= 'localhost',
    #                     password = "postgresql_tutorial",
    #                     port = 5432)

    # ...
