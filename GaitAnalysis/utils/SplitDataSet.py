import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import train_test_split

path = "F:\\data\\gait_maturation\\"

data = pd.read_csv("".join([path, "dataset_list.csv"]))

X = data["index"].values
y = data["age"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(
    X_train, y_train, test_size=0.5, random_state=42)

data_train = data.loc[X_train - 1]
data_val = data.loc[X_val - 1]
data_test = data.loc[X_test - 1]

data_train.to_csv("".join([path, "data_train.csv"]))
data_val.to_csv("".join([path, "data_val.csv"]))
data_test.to_csv("".join([path, "data_test.csv"]))

