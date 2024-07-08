from collections import namedtuple

CreatureNamedTuple = namedtuple(
    typename="CreatureNamedTuple",
    field_names="name, country, area, description, aka",
)
namedtuple_thing = CreatureNamedTuple(
    "yeti",
    "CN",
    "Himalaya",
    "Hirsute HImalayan",
    "Abominable Snowman",
)
print("Example 1: Name is", namedtuple_thing[0])
print("Example 2: Name is", namedtuple_thing.name)
