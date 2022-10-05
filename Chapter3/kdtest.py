from KDTree import KDTree
import numpy as np
from sklearn.datasets import load_iris

Test1=load_iris()
print(type(Test1))
Tdata=Test1.data
label=Test1.target

MyKDTree=KDTree(Tdata[:],label[:])
x=np.array([0,0,0,0])
k=5
MyKDTree.FindKnumNearest(MyKDTree.root, x, k)

print("求k个最近点的距离")
print(sorted([MyKDTree.dis(MyKDTree.L[i].ndata,x) for i in range(k)]))

import heapq
a=[MyKDTree.dis(Tdata[i],x) for i in range(len(Tdata))]
max_number = heapq.nsmallest(k, a)
print("正确答案:")
print(max_number)

