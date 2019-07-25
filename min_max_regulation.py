from sklearn import preprocessing
import numpy as np

income = np.array([5000, 16000, 58000]).reshape(-1,1)
print(income)
min_max_scaler = preprocessing.MinMaxScaler()
minmax_income = min_max_scaler.fit_transform(income)
print(minmax_income)
