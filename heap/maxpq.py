'''最大堆'''

class MaxPQ(object):

    def __init__(self, cap):
        self.pq = [0] * (cap + 1)
        self.N = 0
    
    def parent(self, root):
        return root // 2
    
    def left(self, root):
        return root * 2
    
    def right(self, root):
        return root * 2 + 1

    def max(self):
        return self.pq[1]
    
    def insert(self, e):
        '''插入元素e'''
        self.N += 1
        self.pq[self.N] = e
        self.swim(self.N)

    def delMax(self):
        '''删除并返回堆中的最大元素'''
        max = self.pq[1]
        self.exch(1, self.N)
        self.pq[self.N] = None
        self.N = self.N - 1
        self.sink(1)
        return max

    def swim(self, k):
        '''上浮第k个元素'''
        while (k > 1 and self.less(self.parent(k), k)):
            self.exch(self.parent(k), k)
            k = self.parent(k)
        

    def sink(self, k):
        '''下沉第k个元素'''
        while(self.left(k) <= self.N):
            older = self.left(k)

            if self.right(k) <= self.N and self.less(older, self.right(k)):
                older = self.right(k)
            
            if self.less(older, k):
                break

            self.exch(older, k)
            k = older

    def exch(self, i, j):
        '''交换数组的两个元素'''
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    def less(self, i, j):
        '''判断pq[i]与pq[j]大小'''
        return self.pq[i] < self.pq[j]