#import library pandas dan inisialisasikan menjadi pd
import pandas as pd
#import library numpy dan inisialisasikan menjadi np
import numpy as np
#import library pyplot dari matplotlib dan inisialisasi sebagai plt
from matplotlib import pyplot as plt

#baca data pada file data.csv dalam folder Data menggunakan pandas
data = pd.read_csv('Data/data.csv')

#assign nilai X (Jumlah Klaim) pada variable x
x = data.X.values

#assign nilai Y (Total Pembayaran) pada variable y
y = data.Y.values

#Bagi data menjadi 2 bagian untuk train dan untuk test

#ambil nilai x dari urutan pertama hingga 10 terakhir (108 - 13)
x_train = x[:-10]
#ambil nilai y dari urutan pertama hingga 10 terakhir (392.5 - 31.9)
y_train = y[:-10]


#ambil 10 data terakhir dari x
x_test = x[-10:]
#ambil 10 data terakhir dari y
y_test = y[-10:]

#hitung nilai rata-rata x dan y
x_mean = np.mean(x_train)
y_mean = np.mean(y_train)


#hitung variance x
x_var = np.var(x_train, ddof=1)

#hitung covariance data
cov = np.cov(np.vstack((x_train, y_train)), ddof=1)[0][1]

#hitung nilai b
b = cov / x_var
#hitung nilai a
a = y_mean - (b * x_mean)

#y = xb + a
predict = (x_test * b) + a

#menghitung RMSE model
RMSE = np.sqrt(np.mean(pow(predict - y_test, 2)))


#predict seluruh nilai y untuk seluruh nilai x
predict_all = (x * b) + a

#plot data y berdasarkan x dengan bentuk circle
plt.plot(x, y, 'ro')

#plot data predict_all berdasarkan x
plt.plot(x, predict_all)

#definiskan label untuk garis x
plt.xlabel('Jumlah Tuntutan')
#definisikan label untuk garis y
plt.ylabel('Total Pembayaran')
#tampilkan graph
plt.show()

