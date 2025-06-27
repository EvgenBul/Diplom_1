import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.fixture
    def bun(self):
        return Bun("black bun", 100)

    def test_get_name(self, bun):
        assert bun.get_name() == "black bun"

    def test_get_price(self, bun):
        assert bun.get_price() == 100