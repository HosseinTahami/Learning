from fastapi import FastAPI, Path, Query
from typing import Optional, Union
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    name: str = Path(title="User's Full-Name")
    age: int = Path(gt=0, lt=100, title="User's Age")
    height: Optional[int] = 0
    education: Union[str, None] = None
    sex: bool | None = 0


@app.post("/")
def index(
    person: Person,
    country: str = Query(min_length=2, max_length=30, title="User's Region"),
):
    return {
        "age": person.age,
        "height": person.height,
        "name": person.name,
        "education": person.education,
        "sex": person.sex,
        "country": country,
    }
