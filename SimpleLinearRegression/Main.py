import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np

#baca data pada file data.csv dalam folder Data menggunakan pandas
data = pd.read_csv('Data/data.csv')
#reshape data x dan y dari bentuk (1 row 63 columns ke 63 rows 1 columns)
x = data.X.values.reshape(63, 1)
y = data.Y.values.reshape(63, 1)

#ambil nilai x dari urutan pertama hingga 10 terakhir (108 - 13)
x_train = x[:-10]
#ambil nilai y dari urutan pertama hingga 10 terakhir (392.5 - 31.9)
y_train = y[:-10]


#ambil 10 data terakhir dari x
x_test = x[-10:]
#ambil 10 data terakhir dari y
y_test = y[-10:]

smpReg = linear_model.LinearRegression()


#train model
smpReg.fit(x_train, y_train)

#test model
predict = smpReg.predict(x_test)

#menghitung RMSE model
RMSE = np.sqrt(np.mean(pow(predict - y_test, 2)))

#plot data dan model
figure = plt.figure(1)
plt.plot(x_train, y_train, 'ro')
plt.plot(x, smpReg.predict(x))
plt.xlabel('Jumlah Tuntutan')
plt.ylabel('Total Pembayaran')
plt.show()

