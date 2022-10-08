import numpy as np

x = np.array([
        [2, 7],
        [3, 3],
        [9, 3],
        [6, 7],
        [8, 3],
        [7, 4]])

y = np.array([1, 1, -1, 1, -1, 1])

y = y[np.newaxis, :]
# x = np.array([1, 2, 3, 4])
# print(x)
# print(x.shape)
newx=np.hstack([x,y.T])
print(newx.shape)
print(newx)
np.argmax(x,axis = 0)
# print(x)
# x_add = x[:, np.newaxis]
# x_add2 = x[ np.newaxis,:]
# print(x_add)
# print(x_add2)
# print(x_add.T)
# print(np.hstack((x_add,x_add2.T)))
# print(np.hstack((x,x_add2.T))) wrong 
# np.linalg.norm(x - node.data, ord=2)

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print np.vstack((arr1,arr2))
 
# print np.hstack((arr1,arr2))
 
# a1=np.array([[1,2],[3,4],[5,6]])
# a2=np.array([[7,8],[9,10],[11,12]])
# print a1
# print a2
# print np.hstack((a1,a2))
