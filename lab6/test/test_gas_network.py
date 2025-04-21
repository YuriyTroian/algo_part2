import unittest
from src.gas_network import find_unreachable_cities

class TestGasNetwork(unittest.TestCase):
    def test_partial_reachability(self):
        storages = ["Сховище_1"]
        cities = ["Львів", "Стрий", "Долина"]
        pipelines = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"]
        ]
        result = find_unreachable_cities(storages, cities, pipelines)
        expected = [["Сховище_1", ["Долина"]]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
