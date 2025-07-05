import pytest
from unittest.mock import Mock


class TestBurger:
    # 1. Проверка установки булочки
    def test_set_buns(self, burger, bun_mock):
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    # 2. Проверка добавления ингредиента
    def test_add_ingredient(self, burger, sauce_mock):
        burger.add_ingredient(sauce_mock)
        assert sauce_mock in burger.ingredients
        assert len(burger.ingredients) == 1

    # 3. Проверка удаления ингредиента
    def test_remove_ingredient(self, burger, sauce_mock, filling_mock):
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        burger.remove_ingredient(0)
        assert sauce_mock not in burger.ingredients
        assert filling_mock in burger.ingredients
        assert len(burger.ingredients) == 1

    # 4. Проверка перемещения ингредиента
    def test_move_ingredient(self, burger, sauce_mock, filling_mock):
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [filling_mock, sauce_mock]

    # 5. Проверка расчета цены (параметризованный тест)
    @pytest.mark.parametrize("bun_price, ingredients_prices, expected", [
        (100, [], 200),
        (200, [50], 450),
        (150, [100, 200], 600),
        (0, [0, 0], 0),
        (300, [150, 250, 100], 1100)
    ])
    def test_get_price(self, burger, bun_mock, bun_price, ingredients_prices, expected):
        bun_mock.get_price.return_value = bun_price
        ingredients = []
        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)

        burger.set_buns(bun_mock)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    # 6 Проверка формирования чека
    def test_get_receipt(self, burger, bun_mock, sauce_mock, filling_mock):
        burger.set_buns(bun_mock)
        burger.add_ingredient(sauce_mock)
        burger.add_ingredient(filling_mock)

        expected = (
            "(==== black bun ====)\n"
            "= sauce hot sauce =\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n\n"
            "Price: 400"
        )
        assert burger.get_receipt() == expected