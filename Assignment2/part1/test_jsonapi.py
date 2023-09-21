import unittest
from jsonapi import dumps, loads

class TestJsonAPI(unittest.TestCase):
    
    def test_dumps_with_complex(self):
        obj = [2, 3 + 4j, {'key': 5 + 6j}]
        json_str = dumps(obj)
        self.assertIn('type', json_str)
        self.assertIn('complex', json_str)

    def test_loads_with_complex(self):
        json_str = '[2, {"type": "complex", "real": 3.0, "imag": 4.0}]'
        obj = loads(json_str)
        self.assertIn(3 + 4j, obj)

    def test_dumps_with_range(self):
        obj = list(range(5))
        json_str = dumps(obj)
        expected = '[0, 1, 2, 3, 4]'
        self.assertEqual(json_str, expected)

    def test_loads_with_range(self):
        json_str = '[0, 1, 2, 3, 4]'
        obj = loads(json_str)
        self.assertEqual(obj, list(range(5)))

if __name__ == '__main__':
    unittest.main()
