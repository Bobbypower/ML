import numpy  as np


class Perceptron():
    def __init__(self,data):
        self.b=0
        self.lrate=0.1 #学习率
        self.w=np.zeros(len(data[0])-1,dtype=np.float32)
        print(self.w)
    def sign(self,x,w,b):
        y=np.dot(w,x.T)+b
        return y
    def fit(self,xTrain,yTrain):
        existWrongPoint = False
        while not existWrongPoint:
            wrongPointCount = 0
            for i in range(len(xTrain)):
                x = xTrain[i]
                y = yTrain[i]
                if (y*self.sign(x,self.w,self.b)) <= 0:
                    wrongPointCount = wrongPointCount + 1
                    self.w=self.w + self.lrate*np.dot(y,x)
                    self.b = self.b + self.lrate*y
            if wrongPointCount == 0:
                existWrongPoint = True
        return True



