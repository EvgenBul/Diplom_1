import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.fixture
    def sauce(self):
        return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

    @pytest.fixture
    def filling(self):
        return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

    def test_get_type(self, sauce, filling):
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_name(self, sauce, filling):
        assert sauce.get_name() == "hot sauce"
        assert filling.get_name() == "cutlet"

    def test_get_price(self, sauce, filling):
        assert sauce.get_price() == 100
        assert filling.get_price() == 100