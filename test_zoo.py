import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_invalid_age(self): 
        self.assertEqual(self.zoo.get_ticket_price(-1), 'error')

    def test_age_between_0_and_12(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_age_between_13_and_20(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_age_between_21_and_60(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_age_greater_than_60(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()