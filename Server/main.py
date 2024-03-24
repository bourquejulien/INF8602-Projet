#!/bin/env python3

import logging

from src import container
from src.database_service import Database
from src import login_controller
from flask import Flask
from flask import request
from flask_cors import CORS
import atexit

def init_database():
    container.database = Database("toto", "toto", "localhost", 5432)

    if container.database.is_init():
        return

    data: str = None
    with open("init.sql", "r") as f:
        data = f.read()
        
    container.database.execute_and_commit(data)

def exit_handler():
    if container.database is not None:
        container.database.close()
    logging.info("Exiting...")

def main():
    logging.basicConfig(level=logging.INFO)
    atexit.register(exit_handler)

    init_database()

    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(login_controller.blueprint, url_prefix="/login")
    app.run(host="0.0.0.0")
    

if __name__ == "__main__":
    main()
