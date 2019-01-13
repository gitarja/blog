from utils.PreProcessing import PreProcessing
from utils import Configurations
import pandas as pd
import numpy as np
import glob
class DataGenerator:
    def __init__(self, file_path, dataset_path, T, training=False):
        conf = Configurations
        self.pre_process = PreProcessing(conf.HZT)
        self.T = T
        self.training = training
        self.batch_index = 0
        self.warm_up_time = conf.WARM_UP_TIME
        self.filenames = pd.read_csv(file_path)
        self.dataset_path = dataset_path
        self.num_files = len(self.filenames) - 1


    def open_file(self, index, age):
        filename = "".join([self.dataset_path, str(index)+"-"+str(age)+".txt"])
        data = pd.read_csv(filename, delimiter="\t", header=None)
        data.columns = ["time", "stride"]
        stride = data.loc[data["time"] >= self.warm_up_time]["stride"].values
        len_stride = len(stride)
        sampling = np.arange(0, len_stride, len_stride/self.T).astype(int)
        stride = stride[sampling][:self.T]
        stride = self.pre_process.butter_lowpass_filter(data=stride, cutoff=3.)
        normalized_stride = self.pre_process.scale(stride)
        return normalized_stride

    def generate(self, filepath):
        data = self.open_file(filepath)
        return data["time"].values, data["stride"].values

    def getFlow(self):
        data = []
        self.filenames.sample(frac=1)
        data.append([self.open_file(row["index"], row["age"]) for index, row in self.filenames.iterrows()])
        data = np.array(data).reshape((-1, self.T))

        return np.expand_dims(data, -1), np.expand_dims(self.filenames["age"].values, -1)


