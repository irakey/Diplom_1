import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('ingredient, expected_type', [
        ('sauce', INGREDIENT_TYPE_SAUCE),
        ('filling', INGREDIENT_TYPE_FILLING)
    ])
    def test_ingredient_type(self, request, ingredient, expected_type):
        ingredient_instance = request.getfixturevalue(ingredient)
        assert ingredient_instance.get_type() == expected_type

    @pytest.mark.parametrize('ingredient, expected_name', [
        ('sauce', 'hot sauce'),
        ('filling', 'cutlet')
    ])
    def test_ingredient_name(self, request, ingredient, expected_name):
        ingredient_instance = request.getfixturevalue(ingredient)
        assert ingredient_instance.get_name() == expected_name

    @pytest.mark.parametrize('ingredient, expected_price', [
        ('sauce', 100),
        ('filling', 100)
    ])
    def test_ingredient_price(self, request, ingredient, expected_price):
        ingredient_instance = request.getfixturevalue(ingredient)
        assert ingredient_instance.get_price() == expected_price
