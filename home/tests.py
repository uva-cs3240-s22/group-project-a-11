from django.test import TestCase
from .models import Recipe

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
class TestRecipeModel(TestCase):
    def setUp(self):
        Recipe.object.create(recipeTitle="Reuben",writer="Reiss")
        Recipe.object.create(recipeTitle="Salad",writer="McBurney",vegan=1,glutenfree=1,vegiterian=1)

    def test_options_names_correct(self):
        reuben = Recipe.object.get(recipeTitle="Reuben")
        salad = Recipe.object.get(recipeTitle="Salad")
        self.assertEqual(reuben.writer, "Reiss")
        self.assertEqual(salad.writer, "McBurnery")
        self.assertEqual(reuben.vegan,0)
        self.assertEqual(reuben.vegitarian,0)
        self.assertEqual(reuben.glutenfree,0)
        self.assertEqual(salad.vegan,1)
        self.assertEqual(salad.vegitarian,1)
        self.assertEqual(salad.glutenfree,1)