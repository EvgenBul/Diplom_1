import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database
from praktikum.burger import Burger


@pytest.fixture
def bun():
    return Bun("test bun", 100)

@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def sauce_mock():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100
    return sauce

@pytest.fixture
def filling_mock():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 100
    return filling

@pytest.fixture
def sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture
def filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)