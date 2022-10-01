import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


# iris_data = load_iris()
# iris = iris_data.data
# datax1 = iris[:,0]
# datax2 = iris[:,1]
# targets = iris_data.target
# datax1f1 = datax1[targets==1]
# datax1f0 = datax1[targets==0]
# datax2f1 = datax2[targets==1]
# datax2f0 = datax2[targets==0]

# TestData=[]

# for i in range(len(datax1f1)):
#     TestData.append([datax1f1[i],datax2f1[i],1])
# for i in range(len(datax1f0)):
#     TestData.append([datax1f0[i],datax2f0[i],-1])
# T = np.array(TestData)
#绘制两个类别的点
# plt.scatter(T[T[:,2]==-1][:,0],T[T[:,2]==-1][:,1],label='0')
# plt.scatter(T[T[:,2]==1][:,0],T[T[:,2]==1][:,1],label='1')
# plt.legend()
# # plt.show()



iris_data = load_iris()
print(iris_data.feature_names)
iris = iris_data.data
iris_length = iris[:,0]
iris_width = iris[:,1]
targets = iris_data.target
iris_length_0 = iris_length[targets==0]
iris_width_0 = iris_width[targets==0]
iris_length_1 = iris_length[targets==1]
iris_width_1 = iris_width[targets==1]
T = []
for i in range(len(iris_length_0)):
    T.append([iris_length_0[i],iris_width_0[i],-1])
for i in range(len(iris_length_1)):
    T.append([iris_length_1[i],iris_width_1[i],1])
T = np.array(T)
# plt.scatter(T[T[:,2]==-1][:,0],T[T[:,2]==-1][:,1],label='0')
# plt.scatter(T[T[:,2]==1][:,0],T[T[:,2]==1][:,1],label='0')
# plt.legend()


from PerceptronModel import Perceptron
# from TestData import T
# import matplotlib.pyplot as plt
# import numpy as np


myPerceptron = Perceptron(T)
myPerceptron.fit(T[:,0:2],T[:,2])

x = np.linspace(4,7,10)
# print(x)
print(myPerceptron.w[0])
print(myPerceptron.w[1])

y = -(myPerceptron.w[0]*x+myPerceptron.b)/myPerceptron.w[1]
print(y)
plt.scatter(T[T[:,2]==-1][:,0],T[T[:,2]==-1][:,1],label='0')
plt.scatter(T[T[:,2]==1][:,0],T[T[:,2]==1][:,1],label='1')
plt.show()