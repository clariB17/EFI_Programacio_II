from app.admin import routes
from app.auth import routes

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4