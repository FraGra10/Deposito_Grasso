import numpy as np
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)

df_1 = df.describe()

#print(df_1.loc[["min", "max"]])

range_feature = df.max() - df.min()

print("La feature con la scala più grande è:", range_feature.idxmax())
print("La feature con la scala più piccola è:", range_feature.idxmin())

minmax = MinMaxScaler().fit(df)

df_mm = minmax.transform(df)

print(df_mm.min(axis=0))
print(df_mm.max(axis=0))
