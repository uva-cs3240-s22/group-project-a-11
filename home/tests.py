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