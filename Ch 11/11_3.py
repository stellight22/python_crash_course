import unittest
from employee import Employee

class Emp_Test(unittest.TestCase):

    def setUp(self):
        self.jj = Employee('Jolene', 'Jakyl', 300000)
        self.rj = Employee('Roland', 'Justin', 200000)

    def test_default_raise(self):
        self.jj.give_raise()
        self.assertEqual(self.jj.salary,305000)

    def test_custom_raise(self):
        self.rj.give_raise(9000)
        self.assertEqual(self.rj.salary, 209000)

unittest.main()


