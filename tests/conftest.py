import pytest


@pytest.fixture
def bun():
    from praktikum.bun import Bun
    return Bun("test bun", 100)

@pytest.fixture
def ingredient():
    from praktikum.ingredient import Ingredient
    from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)

@pytest.fixture
def database():
    from praktikum.database import Database
    return Database()

@pytest.fixture
def burger():
    from praktikum.burger import Burger
    return Burger()