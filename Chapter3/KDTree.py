import numpy as np


class KDNode(object):
    def __init__(self, ndata, split, left, right, target):
        self.ndata = ndata
        self.split = split
        self.left = left
        self.right = right
        self.case = 0  # 0表示还未被访问
        self.label = target
        print("我是"+str(ndata)),
        # print(self.left)

    def __str__(self):
        # print("左是"+str(self.left))
        return "左是"+str(self.label)

class KDTree:
    def __init__(self, data,target):
        # self.data = np.array(data)
        self.data = data

        self.k = len(data[0])
        self.label = target
        self.root = self.creatnode(data, 0)
        self.L = []

    def creatnode(self, data, split):
        
        if data == []:
            return None
        SplitPos = len(data)//2
        DataSorted = sorted(data, key=lambda x: x[split])

        for i in range(len(self.data)):
            if (self.data[i] == DataSorted[SplitPos]).all():
                break

        median = DataSorted[SplitPos]
        SplitNext = (split+1) % self.k
        print(str(split)+"层"+"---第"+str(i)+"个")
        # print(KDNode(median, split, self.creatnode(DataSorted[:SplitPos], SplitNext), self.creatnode(DataSorted[SplitPos+1:], SplitNext), self.label[i]))
        return KDNode(median, split, self.creatnode(DataSorted[:SplitPos], SplitNext), self.creatnode(DataSorted[SplitPos+1:], SplitNext), self.label[i])

    def FindNearest(self, tree, point):

        self.NearestPoint = None
        self.NearestValue = 0

        def travel(node, depth):
            # 遍历kd树
            if node != None:
                n=len(point)
                axis=depth%n
                if point[axis]<node.nadta[axis]:
                    travel(node.left, depth+1)
                else:
                    travel(node.right, depth+1)

            D=self.dis(point,node.ndata)

            if node.left is None and node.right is None:
                node.case=1
                if len(self.L)<k:
                    self.l.append(node)
                elif len(self.L)==k:
                    [ind,di] = self.maxdis(self.L,point)
                    if di > D:
                        self.L[ind] =node
            if abs(point[axis]-node.ndata[axis]) < di or len(self.L)<k:
                if point[axis]<node.ndata[axis]:
                    travel(node.right,depth+1)
                else:
                    travel(node.left, depth+1)

        travel(tree, 0)
        return self.NearestPoint
    def FindKnumNearest(self,tree,point,k):
        self.L=[]
        def travel(node,depth):
            if node != None:
                n=len(point)
                axis=depth%n  #第depth层代表以第depth%n维度切分
                if point[axis]<node.ndata[axis]:
                    travel(node.left,depth+1)
                else:
                    travel(node.right,depth+1)
                distance=self.dis(point,node.ndata)#与当前结点的距离
 
                if node.left is None and node.right is None:#判断是否为叶子结点
                    node.case=1 #若叶子结点，标记已访问过
                    if len(self.L)<k:
                        self.L.append(node)
                    elif len(self.L)==k:
                        [ind,di]=self.maxdis(self.L,point)
                        if di>distance:
                            self.L[ind]=node#替换最大距离为此结点
 
                #执行a
                if node.case==0:
                    node.case=1
                    if len(self.L)<k:
                        self.L.append(node)
                        di=0
                    else :
                        [ind, di] = self.maxdis(self.L, point)
                        if di > distance:
                            self.L[ind] = node
 
                    if abs(point[axis] - node.ndata[axis]) < di or len(self.L) < k:
                        if point[axis]<node.ndata[axis]:#这代表上一次是向左边遍历的，所以这一次直接向右边
                            travel(node.right,depth+1)
                        else:#同理
                            travel(node.left,depth+1)
        travel(tree,0)
        self.DFS(tree)
    def DFS(self,node):
        if node is None:
            return 
        node.case=0
        self.DFS(node.left)
        self.DFS(node.right)

    def maxdis(self,L,point):
        p=[]
        for i in L:
            p.append(self.dis(i.ndata,point))
        ind=p.index(max(p))
        di=p[ind]
        return ind,di

    def dis(self,a,b):
        return ((np.array(a)-np.array(b))**2).sum()**0.5

        