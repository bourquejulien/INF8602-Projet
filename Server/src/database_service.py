import logging

from .classes.user import User
from .classes.login_info import LoginInfo
import psycopg
from psycopg import Connection

DATABASE_NAME = "users"

class Database:
    connection: Connection

    def __init__(self, username: str, password: str, host: str, port: int) -> None:
        self.connection = psycopg.connect(f"dbname={DATABASE_NAME} user={username} host={host} password={password} port={port}")

    def login(self, login_info: LoginInfo) -> User | None:
        user: User = None

        result = self.execute(f"select * from users where username = '{login_info.username}'")[0]

        if result is None:
            return None
        
        user = User(*result)
        
        if user.password != login_info.password:
            return None
        
        return user
    
    def is_init(self):
        result = self.execute(f"SELECT to_regclass('public.{DATABASE_NAME}');")
        return result[0][0] is not None
    
    def execute_and_commit(self, payload: str):
        self.execute(payload)
        self.connection.commit()
    
    def execute(self, payload: str):
        with self.connection.cursor() as cur:
            try:
                cur.execute(payload)
            except Exception as e:
                logging.exception("Failed to execute command")
                self.connection.rollback()

            if cur.rowcount == -1:
                return []
            
            return cur.fetchall()

    def close(self):
        self.connection.close()
