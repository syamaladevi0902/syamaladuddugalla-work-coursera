from my_project import app

def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0

def test_subtract():
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 3) == -3
