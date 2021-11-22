import unittest
from name_function import add_two, get_formatted_name
from build_profile import build_profile

class NamesTest(unittest.TestCase):  # TestCase is a class within unittest, a superclass that NamesTest inherits

    def test_first_last_name(self):
        full_name = get_formatted_name('phyllis', 'Doe' )
        self.assertEqual(full_name, 'Phyllis Doe')
    
    def test_all_three(self):
        complete_name = get_formatted_name('cookie', 'Jr.','monster')
        self.assertEqual(complete_name, 'Cookie Monster Jr.')

    def test_sum(self):
        math1 = add_two(4,5)
        self.assertEqual(math1, 9)

    def test_build_profile(self):
        profile = build_profile('Jimmy', 'hula', drink = 'pina colada')
        self.assertEqual(profile['first_name'], 'Jimmy')


unittest.main()
#unindented and unconstrained
#when unittest. is read, unittest functions is called in which there's different attr and methods
#one of which TestCase class is checking for its related child classes
#NamesTest is a child class, as noted by the superclass TestCase
#within NamesTest the methods with "test_" beginning become executed
#TestCase class is instantiated

#once unittest is called, it exists




#unittest.TestCase. can see all the methods