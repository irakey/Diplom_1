import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize('name, price', [
    ('Краторная булка N-200i', 1255),
    ('Флюоресцентная булка R2-D3', 988),
])
class TestBun:
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price