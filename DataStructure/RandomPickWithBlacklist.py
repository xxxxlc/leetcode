# 给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。

# 对它进行优化使其尽量少调用系统方法 Math.random() 。

import random

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.N = N
        self.mapping = dict()
        sz = N - len(blacklist)

        for b in blacklist:
            self.mapping[b] = 666
        
        last = N - 1
        for b in blacklist:
            if b >= sz:
                continue
            while(last in self.mapping.keys()):
                last -= 1
            
            self.mapping[b] = last
            last -= 1
        

    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.N - 1)

        if index in self.mapping.keys():
            return self.mapping[index]
        
        return index