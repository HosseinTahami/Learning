from model.creature import Creature

_creatures = [
    Creature(
        name="Yeti",
        aka="Abominable Snowman",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
    ),
    Creature(
        name="Bigfoot",
        country="US",
        area="*",
        aka="Sasquatch",
        description="Yeti's Cousin Eddie"
    ),
]


def get_all() -> list[Creature]:
    """Return all Creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    """Create a new Creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially Modify an Creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely Replace an Creature"""
    return creature


def delete(creature: Creature) -> Creature:
    """Delete an Creature; return Non if it existed"""
    return None
