from utils.PreProcessing import PreProcessing
from utils import Configurations
import pandas as pd
import numpy as np
import glob
class DataGenerator:
    def __init__(self, batch_size, dataset_path, T, training=False):
        conf = Configurations
        self.pre_process = PreProcessing(conf.HZT)
        self.T = T
        self.training = training
        self.batch_index = 0
        self.warm_up_time = conf.WARM_UP_TIME
        self.batch_size = batch_size
        self.filenames = glob.glob("".join([dataset_path, "*.txt"]))
        self.num_files = len(self.filenames) - 1


    def open_file(self, filepath):
        data = pd.read_csv(filepath, delimiter="\t", header=None)
        data.columns = ["time", "stride"]
        stride = data.loc[data["time"] >= self.warm_up_time]["stride"].values
        len_stride = len(stride)
        sampling = np.arange(0, len_stride, len_stride/self.T).astype(int)
        stride = stride[sampling][:self.T]
        return stride

    def generate(self, filepath):
        data = self.open_file(filepath)
        return data["time"].values, data["stride"].values

    def getFlow(self, batch_index):
        if ((batch_index+1)*self.batch_size) <= self.num_files:
            filenames = self.filenames[batch_index*self.batch_size:(batch_index+1)*self.batch_size]
        else:
            filenames = self.filenames[self.num_files-self.batch_size:self.num_files]

        data = []
        data.append([self.open_file(file) for file in filenames])
        data = np.array(data).reshape((self.batch_size, self.T, -1))

        return data


