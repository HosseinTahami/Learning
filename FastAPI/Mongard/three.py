from fastapi import FastAPI
from typing import Optional, Union
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str
    age: int
    height: Optional[int] = 0
    education: Union[str, None] = None
    sex: bool | None = 0

@app.post("/")
def index(person: Person):
    return {
        "age": person.age,
        "height": person.height,
        "name": person.name,
        "education": person.education,
        "sex": person.sex
    }
