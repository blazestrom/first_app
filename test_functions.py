import unittest

from functions import Functions

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self._function = Functions()

    def TearDown(self):
        pass

    def test_calculator_add(self):
        result = self._function.calculator("add",2,8)
        self.assertEqual(result,10)
        self.assertIsInstance(result,int)

    def test_calculator_sub(self):
        result = self._function.calculator("sub",2,8)
        self.assertEqual(result,-6)
        self.assertIsInstance(result,int)

    def test_calculator_mul(self):
        result = self._function.calculator("mul",2,8)
        self.assertEqual(result,16)
        self.assertIsInstance(result,int)

    def test_calculator_div(self):
        result = self._function.calculator("div",24,8)
        self.assertEqual(result,3)
        self.assertIsInstance(result,float)



    def test_calculator_else(self):
        result = self._function.calculator("cube",25,8)
        self.assertEqual(result,"incorrect op")
        self.assertIsInstance(result,str)

    def test_calculator_sqrt(self):
        result = self._function.calculator("sqrt",25,8)
        self.assertEqual(result,625)
        self.assertIsInstance(result,int)




