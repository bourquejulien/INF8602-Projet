#!/bin/env python3

import logging

from src import container
from src.database_service import Database
from src import info_controller, login_controller
from flask import Flask
from flask import request
from flask_cors import CORS
import atexit

def exit_handler():
    container.database.close()
    logging.info("Exiting...")

def main():
    logging.basicConfig(level=logging.INFO)
    container.database = Database("toto", "toto", "localhost", 5432)
    atexit.register(exit_handler)

    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(login_controller.blueprint, url_prefix="/login")
    app.register_blueprint(info_controller.blueprint, url_prefix="/info")
    app.run(host="0.0.0.0")
    

if __name__ == "__main__":
    main()
