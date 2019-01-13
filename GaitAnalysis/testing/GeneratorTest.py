import unittest
# from utils.Generator import DataGenerator
from utils.DiscriminatorGenerator import DataGenerator
import numpy as np
import matplotlib.pyplot as plt
class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     file_path = "F:\\data\\gait_maturation\\"
    #     generator = DataGenerator(batch_size=1, dataset_path=file_path, T=256)
    #     x = generator.getFlow(1)
    #     plt.plot(x[0])
    #     plt.show()
    #     # data = []
    #     # for i in range(10):
    #     #     data.append(generator.getFlow(i))
    #     #
    #     # data = np.array(data)
    #     self.assertEqual(True, True)


    def test_discriminator_gen(self):
        dataset_path = "F:\\data\\gait_maturation\\"
        file_path = "".join([dataset_path, "dataset_list.csv"])
        generator = DataGenerator(file_path=file_path, dataset_path=dataset_path, T = 200)
        X, y = generator.getFlow()

        self.assertEqual(X.shape[0], y.shape[0])


if __name__ == '__main__':
    unittest.main()
