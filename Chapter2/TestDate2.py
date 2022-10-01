import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data,columns=iris.feature_names)
print(iris.feature_names)
df['label'] = iris.target
df.columns=['sepal length','sepal width','petal length','petal width','label']
df.label.value_counts()
# print(df[:50])
print(df[50:100])

# plt.scatter(df[:50]['sepal length'],df[:50]['sepal width'],label='0')
# plt.scatter(df[50:100]['sepal length'],df[50:100]['sepal width'],label='1')
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.legend()
# plt.show()