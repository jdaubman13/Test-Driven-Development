import pytest

@pytest.fixture
def player():
    return {"health": 80, "max_health": 100, "alive": True}

@pytest.fixture
def game():
    return {"score": 0, "multiplier": 1, "active": True}

@pytest.fixture
def empty_inventory():
    return {"items": [], "capacity": 10, "locked": False}

@pytest.fixture
def full_inventory():
    return {"items": ["a"] * 10, "capacity": 10, "locked": False}

@pytest.fixture
def locked_inventory():
    return {"items": ["sword"], "capacity": 10, "locked": True}
