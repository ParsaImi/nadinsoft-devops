from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1 , 2)

    def test_basic_substraction(self):
        self.assertEqual(2 - 1 , 1)

    def test_basic_multiplication(self):
        self.assertEqual(2 * 2, 4)
