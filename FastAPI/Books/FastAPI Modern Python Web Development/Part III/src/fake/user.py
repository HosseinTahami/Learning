from model.user import User
from error import Missing, Duplicate

fakes = [
    User(
        name="one",
        hash="abc",
    ),
    User(
        name="two",
        hash="123",
    ),
]

def find(name: str) -> User | None:
    for user in fakes:
        if user.name == name:
            return user
        return None