import pandas as pd
import numpy as np

from scipy import signal
class PreProcessing:
    def __init__(self, fs):
        self.fs = fs



    def butter_highpass(self, cutoff, fs, order=5):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_highpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_highpass(cutoff, fs, order=order)
        y = signal.filtfilt(b, a, data)
        return y

    def scale(self, data):
        data = self.butter_highpass_filter(data, cutoff=4.5, fs=self.fs, order=5)
        max = np.max(data)
        min = np.min(data)

        return (data - min) / (max - min)

    def spatial_result(self, data):
        if data is not None:
            data = self.butter_highpass_filter(data, cutoff=4.5, fs=self.fs, order=5)
            f, power = signal.welch(data, self.fs)
            return f, power
