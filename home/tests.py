from django.test import TestCase
from .models import Ingredients, Recipe, Step,Tag

# Create your tests here.
"""
Author: Jesse Unruh Garcia
Input: two Recipe Models, one with a recipe for a Reuben written by writer Reiss
        the other for a recipe for a Salad written by writer Mcburner,
        the salad is vegan, glutenfree, and vegitarian
Output: Both the Reuben and Salad can be found by their recipe names,
        Reiss is found to be the author of the Reuben, its vegan, vegetarian,
        and glutenfree values are equal to 0
        McBurney is found to be the author of the Salad, its vegan, vegetarian,
        and glutenfree values are equal to 1
Type of Test: Equivalency
User Story ID: 5
"""


"""
Author: Kasra Lekan
Input: a recipe model and an ingredient model
Type of Test: Equivalency
"""
class RecipeTestCase(TestCase):
    def setUp(self):
        recipe = Recipe.objects.create(recipeTitle="cooked_bacon", recipeText="Cooked Bacon")
        Ingredients.objects.create(recipe=recipe, name="water", units="mg", quantity="3")

    def test_recipe_text_equivalence(self):
        cooked_bacon = Recipe.objects.get(recipeTitle="cooked_bacon")
        self.assertEqual(str(cooked_bacon), 'cooked_bacon')
        self.assertEqual(cooked_bacon.recipeText, 'Cooked Bacon')
        
    def test_recipe_like_count(self):
        cooked_bacon = Recipe.objects.get(recipeTitle="cooked_bacon")
        self.assertEqual(cooked_bacon.total_likes(), 0)

    def test_ingredient_text_equivalence(self):
        water = Ingredients.objects.get(name="water")
        self.assertEqual(water.name, 'water')
        self.assertEqual(water.units, 'mg')
        self.assertEqual(water.quantity, 3)
        
    def test_recipe_add_ingredient(self):
        cooked_bacon = Recipe.objects.get(recipeTitle="cooked_bacon")
        water = Ingredients.objects.get(name="water")
        self.assertEqual(water.recipe, cooked_bacon)

