from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDataBase:

    def test_available_buns_name(self):
        data = Database()
        available_buns = data.available_buns()
        assert available_buns[0].get_name() == "black bun"
        assert available_buns[1].get_name() == "white bun"
        assert available_buns[2].get_name() == "red bun"

    def test_available_buns_price(self):
        data = Database()
        available_buns = data.available_buns()
        assert available_buns[0].get_price() == 100
        assert available_buns[1].get_price() == 200
        assert available_buns[2].get_price() == 300

    def test_available_ingredients_name(self):
        data = Database()
        available_ingredients = data.available_ingredients()
        assert available_ingredients[0].get_name() == "hot sauce"
        assert available_ingredients[1].get_name() == "sour cream"
        assert available_ingredients[2].get_name() == "chili sauce"
        assert available_ingredients[3].get_name() == "cutlet"
        assert available_ingredients[4].get_name() == "dinosaur"
        assert available_ingredients[5].get_name() == "sausage"

    def test_available_ingredients_price(self):
        data = Database()
        available_ingredients = data.available_ingredients()
        assert available_ingredients[0].get_price() == 100
        assert available_ingredients[1].get_price() == 200
        assert available_ingredients[2].get_price() == 300
        assert available_ingredients[3].get_price() == 100
        assert available_ingredients[4].get_price() == 200
        assert available_ingredients[5].get_price() == 300

    def test_available_ingredients_type(self):
        data = Database()
        available_ingredients = data.available_ingredients()
        assert available_ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert available_ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert available_ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert available_ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
