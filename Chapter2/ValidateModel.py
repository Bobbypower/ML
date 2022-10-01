from PerceptronModel import Perceptron
from TestData import T
import matplotlib.pyplot as plt
import numpy as np


myPerceptron = Perceptron(T)
myPerceptron.fit(T[:,0:2],T[:,2])

x = np.linspace(4,7,10)
y = -(myPerceptron.w[0]*x+myPerceptron.b)/myPerceptron.w[1]
plt.plot(x,y)
plt.scatter(T[T[:,2]==-1][:,0],T[T[:,2]==-1][:,1],label='0')
plt.scatter(T[T[:,2]==1][:,0],T[T[:,2]==1][:,1],label='1')
plt.show()