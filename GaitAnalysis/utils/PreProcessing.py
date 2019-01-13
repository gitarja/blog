import pandas as pd
import numpy as np
from utils import Configurations

from scipy import signal
class PreProcessing:
    def __init__(self, fs):
        self.fs = fs
        self.conf = Configurations




    def butter_lowpass(self, cutoff, order=5):
        nyq = 0.5 * self.fs
        normal_cutoff = cutoff / nyq
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, order=5):
        b, a = self.butter_lowpass(cutoff, order=order)
        y = signal.filtfilt(b, a, data)
        return y

    def scale(self, data):
        return (data - self.conf.MIN_SIG_VAL) / (self.conf.MAX_SIG_VAL - self.conf.MIN_SIG_VAL)

    def spatial_result(self, data):
        if data is not None:
            f, power = signal.welch(data, self.fs)
            return f, power
