import logging

from .classes.database_info import DatabaseInfo
from .classes.user import User
from .classes.login_info import LoginInfo
import psycopg
from psycopg import Connection

DATABASE_NAME = "users"

class Database:
    connection: Connection
    database_info: DatabaseInfo
    is_safe: bool

    def __init__(self, database_info: DatabaseInfo, is_safe: bool) -> None:
        self.is_safe = is_safe
        self.database_info = database_info
        self._connect(should_fail=True)

    def login(self, login_info: LoginInfo) -> User | None:
        user: User = None

        if self.is_safe:
            results = self.execute("select * from users where username = %s", login_info.username)
        else:
            results = self.execute(f"select * from users where username = '{login_info.username}'")

        if len(results) == 0 or results[0] is None:
            return None
        
        user = User(*results[0])
        
        if user.password != login_info.password:
            return None
        
        return user
    
    def is_init(self):
        result = self.execute(f"SELECT to_regclass('public.{DATABASE_NAME}');")
        return result[0][0] is not None
    
    def execute_and_commit(self, payload: str):
        self.execute(payload)
        self.connection.commit()
    
    def execute(self, payload: str, *args: str):
        if self.connection.closed != 0:
            self._connect()

        with self.connection.cursor() as cur:
            try:
                cur.execute(payload, args)
            except Exception as e:
                logging.exception("Failed to execute command")
                self.connection.rollback()

            if cur.rowcount == -1:
                return []
            
            return cur.fetchall()

    def close(self):
        self.connection.close()

    def _connect(self, should_fail: bool = False):
        try:
            self.connection = psycopg.connect(f"dbname={DATABASE_NAME} user={self.database_info.username} host={self.database_info.address} password={self.database_info.password} port={self.database_info.port}")
        except Exception as e:
            logging.exception("Failed to connect to database")
            if should_fail:
                raise e
