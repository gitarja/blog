import unittest
from utils.Generator import DataGenerator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        file_path = "D:\\usr\\pras\\data\\experiment\\gaitAnalysis\\data\\"
        generator = DataGenerator(batch_size=5, dataset_path=file_path, T=256)
        generator.getFlow(1)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
