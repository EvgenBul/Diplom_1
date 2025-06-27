import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    @pytest.fixture
    def burger(self):
        return Burger()

    @pytest.fixture
    def bun_mock(self):
        bun = Mock()
        bun.get_name.return_value = "black bun"
        bun.get_price.return_value = 100
        return bun

    @pytest.fixture
    def sauce_mock(self):
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "hot sauce"
        sauce.get_price.return_value = 100
        return sauce

    @pytest.fixture
    def filling_mock(self):
        filling = Mock()
        filling.get_type.return_value = "FILLING"
        filling.get_name.return_value = "cutlet"
        filling.get_price.return_value = 100
        return filling

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
        (100, [], 200),  # Только булочка
        (200, [50], 450),  # Булочка + 1 ингредиент
        (150, [100, 200], 600),  # Булочка + 2 ингредиента
        (0, [0, 0], 0),  # Нулевая стоимость
        (300, [150, 250, 100], 1100)  # Булочка + 3 ингредиента
    ])
    def test_get_price(self, burger, bun_mock, bun_price, ingredients_prices, expected):
        bun_mock.get_price.return_value = bun_price

        # Создаем моки ингредиентов с заданными ценами
        ingredients = []
        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            ingredients.append(ingredient)

        # Собираем бургер
        burger.set_buns(bun_mock)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    # 6 Проверка формирования чека
    def test_get_receipt(self, burger, bun_mock, sauce_mock, filling_mock):
        bun_mock.get_name.return_value = "black bun"
        sauce_mock.get_type.return_value = "SAUCE"
        sauce_mock.get_name.return_value = "hot sauce"
        filling_mock.get_type.return_value = "FILLING"
        filling_mock.get_name.return_value = "cutlet"

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