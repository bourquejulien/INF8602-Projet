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
        with self.connection.cursor() as cur:
            try:
                cur.execute(f"select * from users where username = '{login_info.username}'")
            except Exception as e:
                print(f'Error {e}')
                self.connection.rollback()
            result = cur.fetchone()

            if result is None:
                return None
            
            user = User(*result)
        
        if user.password != login_info.password:
            return None
        
        return user 
    
    def close(self):
        self.connection.close()
