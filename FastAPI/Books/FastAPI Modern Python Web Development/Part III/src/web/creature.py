from fastapi import APIRouter

from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix="/creature")

@router.get("/")
def top():
    return "top creature endpoint"

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one() -> Creature:
    return service.get_one()

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)