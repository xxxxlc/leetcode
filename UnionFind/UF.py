
class UF(object):
    
    
    def __init__(self, n):
        self.__count = n
        self.__parent = []
        # 重量数组，避免数据头重脚轻
        self.__size = []

        for i in range(0, n):
            self.__parent.append(i)

            # 最初每棵数只有一个节点，所以初始重要为1
            self.__size.append(1)

        


    def union(self, p, q):
        '''
        将p和q相连
        '''
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        # 将p的根节点接到q的根节点下
        # self.__parent[rootP] = rootQ   
        # self.__count = self.__count - 1

        if self.__size[rootP] > self.__size[rootQ]:
            self.__parent[rootQ] = rootP
            self.__size[rootP] += self.__size[rootQ]
        
        else:
            self.__parent[rootP] = rootQ
            self.__size[rootQ] += self.__size[rootP]
    
    def find(self, x):
        '''
        找到x节点的根节点, 根节点parent的值与自身相等
        '''
        while(self.__parent[x] != x):
            self.__parent[x] = self.__parent[self.__parent[x]]
            x = self.__parent[x]
        
        return x

    def connected(self, p, q):
        '''
        判断p和q是否相连
        '''
        rootP = self.find(p)
        rootQ = self.find(q)

        return  rootP == rootQ
            


    def count(self):
        '''
        返回图中有多少个连通分量
        '''
        return self.__count
