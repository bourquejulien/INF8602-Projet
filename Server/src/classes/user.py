from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
