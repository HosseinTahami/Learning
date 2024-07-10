from model.creature import Creature
from service import creature as code

sample = Creature(
    name="Yeti",
    area="Himalayas",
    country="CN",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",
)

def test_create():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample

def test_get_one():
    resp = code.get_one("box-turtle")
    assert resp is None
    
"""
pytest -v test/unit/service/test_creature.py
=================================================================================== test session starts ====================================================================================
platform linux -- Python 3.11.7, pytest-8.2.2, pluggy-1.5.0 -- /home/Hossein/Personal/Programming/Projects/Learning/FastAPI/Books/FastAPI Modern Python Web Development/Part III/src/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/Hossein/Personal/Programming/Projects/Learning/FastAPI/Books/FastAPI Modern Python Web Development/Part III/src
plugins: anyio-4.4.0
collected 3 items                                                                                                                                                                          

test/unit/service/test_creature.py::test_create PASSED                                                                                                                               [ 33%]
test/unit/service/test_creature.py::test_get_exists PASSED                                                                                                                           [ 66%]
test/unit/service/test_creature.py::test_get_one PASSED                                                                                                                              [100%]

==================================================================================== 3 passed in 0.05s =====================================================================================
"""