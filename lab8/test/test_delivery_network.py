import unittest
import os
import sys

# Додаємо src до шляху
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from delivery_network import DeliveryNetwork


class TestDeliveryNetwork(unittest.TestCase):
    def setUp(self):
        self.network = DeliveryNetwork()
        file_path = os.path.join(os.path.dirname(__file__), "../roads.csv")
        self.network.load_from_csv(file_path)

    def test_max_flow(self):
        self.assertEqual(self.network.max_flow(), 5)


if __name__ == "__main__":
    unittest.main()
