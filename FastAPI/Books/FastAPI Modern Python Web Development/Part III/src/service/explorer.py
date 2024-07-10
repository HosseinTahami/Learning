from model.explorer import Explorer
import fake.explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()


def get_one(name: str) -> Explorer | None:
    return data.get_one(id)


def create(explorer: Explorer) -> Explorer:
    return data.create()


def replace(id, explorer: Explorer) -> Explorer:
    return data.replace(id, explorer)


def modify(id, explorer: Explorer) -> Explorer:
    return data.modify(id, explorer)

def delete(id, explorer: Explorer) -> bool:
    return data.delete()
