from dataclasses import dataclass

@dataclass
class DatabaseInfo:
    username: str
    password: str
    address: str
    port: int
