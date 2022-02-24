from django.test import TestCase

class QuestionModelTests(TestCase):

    def test_true(self):
        """
        test_true() returns True regardless.
        """
        self.assertIs(True, False)
