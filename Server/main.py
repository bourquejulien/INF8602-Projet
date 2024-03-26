#!/bin/env python3

import logging

from src.classes.database_info import DatabaseInfo
from src import container
from src.database_service import Database
from src import login_controller
from flask import Flask
from flask_cors import CORS
import atexit
import sys
import os

DEFAULT_ADDRESS = "localhost"
DEFAULT_PORT = 5432

def init_database(database_info: DatabaseInfo, is_safe: bool):
    container.database = Database(database_info, is_safe)

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

def main(address: str, port: int, is_safe: bool):
    logging.basicConfig(level=logging.INFO)
    atexit.register(exit_handler)

    init_database(DatabaseInfo("toto", "toto", address, port), is_safe)
    logging.info("Connected to Database with: %s:%d", address, port)

    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(login_controller.blueprint, url_prefix="/login")
    app.run(host="0.0.0.0")

if __name__ == "__main__":
    address = DEFAULT_ADDRESS
    port = DEFAULT_PORT

    if len(sys.argv) > 1:
        address = sys.argv[1]

    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    is_safe = "IS_SAFE" in os.environ and os.environ["IS_SAFE"].lower() == "true"
        
    main(address, port, is_safe)
