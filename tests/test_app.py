import sys
import os

# Ensure Python can find the 'my_project' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_project import app


def test_add():
    """Test the add function."""
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0


def test_subtract():
    """Test the subtract function."""
    assert app.subtract(5, 3) == 2
    assert app.subtract(0, 3) == -3
