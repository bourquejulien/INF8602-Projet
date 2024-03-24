from .classes.user import User
from .classes.login_info import LoginInfo
import psycopg
from psycopg import Connection

DATABASE_NAME = "USERS"

class Database:
    connection: Connection

    def __init__(self, username: str, password: str, host: str, port: int) -> None:
        self.connection = psycopg.connect(f"dbname={DATABASE_NAME} user={username} host={host} password={password} port={port}")

    def get_info(login_info: LoginInfo) -> User:
        ...
    
    def close(self):
        self.connection.close()
