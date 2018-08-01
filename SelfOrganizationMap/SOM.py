import numpy as np
from math import log
from math import exp
import matplotlib.pyplot as plt


class SOM:
    def __init__(self, trainData, N):
        self.N = N
        x, y = np.meshgrid(range(self.N), range(self.N))
        self.dMapRadius = self.N / 2

        self.learningRate = 0.1
        self.k = trainData.shape[0] / log(self.dMapRadius)

        self.tp = np.hstack((x.flatten()[:, np.newaxis],
                            y.flatten()[:, np.newaxis]))

        self.w = np.random.rand(self.N*self.N,
                                trainData.shape[1])
        self.trainData = trainData




    def train(self):
        for t, x in enumerate(self.trainData):
            bmu = self.find_BMU(w=self.w, x=x)
            S = np.linalg.norm(self.tp - bmu, axis=1)
            sigma = self.dMapRadius * exp(-t/self.k)
            learn_radius = np.exp(- ((S ** 2) / (2 * sigma ** 2)))
            learn_ratio = self.learningRate * exp(-t/self.k)
            self.w += learn_ratio * learn_radius[:, np.newaxis] * (x - self.w)
        return self.w



    def find_BMU(self, w, x):
        dx = np.linalg.norm(w - x, axis=1)
        bmu = np.argmin(dx)
        return np.unravel_index(bmu, (self.N, self.N))




N = 20
trainData = np.random.random((10000, 3))
som = SOM(trainData=trainData, N = N)


plt.imshow(som.w.reshape((N, N, 3)),
           interpolation='none')
plt.show()

som.train()
plt.imshow(som.w.reshape((N, N, 3)),
           interpolation='none')
plt.show()
