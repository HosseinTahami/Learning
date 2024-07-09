from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Hossein Tahami",
        country="IR",
        description="Code King",
    ),
    Explorer(
        name="Real Madrid",
        country="SP",
        description="King of Europe",
    ),
]


def get_all() -> list[Explorer]:
    """Return All Explorers"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """Create a new Explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partially Modify an Explorer"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Completely Replace an Explorer"""
    return explorer


def delete(explorer: Explorer) -> Explorer:
    """Delete an Explorer; return Non if it existed"""
    return None
