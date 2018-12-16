import unittest
from utils.Generator import DataGenerator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        file_path = "F:\\data\\gait_maturation\\"
        generator = DataGenerator(batch_size=5, dataset_path=file_path, T=256)
        data = generator.getFlow(1)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
