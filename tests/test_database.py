from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestDataBase:

    def test_available_buns(self):
        data = Database()
        available_buns = data.available_buns()
        assert available_buns[0].get_name() == "black bun"
        assert available_buns[0].get_price() == 100

    def test_available_ingredients_positive(self):
        data = Database()
        available_ingredients = data.available_ingredients()
        assert available_ingredients[0].get_name() == "hot sauce"
        assert available_ingredients[0].get_price() == 100
        assert available_ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE