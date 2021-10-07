from temperature import Temperature
import unittest

celsius_test1 = Temperature(celsius=20)
fahrenheit_test1 = Temperature(fahrenheit=50)
celsius_test2 = Temperature(celsius=1)
fahrenheit_test2 = Temperature(fahrenheit=100)  

class temp_test(unittest.TestCase):
    def test_celsius(self):
        self.assertEqual(celsius_test1.kelvin, 293.15) # This must be ok since the values are equal

    def test_fahrenheit(self):
        self.assertEqual(fahrenheit_test1.kelvin, 283.15) # This must be ok since the values are equal

    def test_celsius2(self):
        self.assertEqual(celsius_test2.kelvin, 274.15) # This must be ok since the values are equal

    def test_fahrenheit2(self):
        self.assertEqual(fahrenheit_test2.kelvin, 310.93) # This must be failed since the values are not equal

if __name__ == "__main__":
    unittest.main()