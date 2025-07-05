from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_get_type(self, sauce, filling):
        assert sauce.get_type() == INGREDIENT_TYPE_SAUCE
        assert filling.get_type() == INGREDIENT_TYPE_FILLING

    def test_get_name(self, sauce, filling):
        assert sauce.get_name() == "hot sauce"
        assert filling.get_name() == "cutlet"

    def test_get_price(self, sauce, filling):
        assert sauce.get_price() == 100
        assert filling.get_price() == 100