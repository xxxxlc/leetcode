# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。

# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.valToIndex = dict()


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.valToIndex.keys():
            return False
        
        else:
            self.valToIndex[val] = len(self.nums)
            self.nums.append(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.valToIndex.keys():
            return False
        
        index = self.valToIndex[val]
        self.valToIndex[self.nums[-1]] = index
        temp = self.nums[-1]
        self.nums[-1] = val
        self.nums[index] = temp
        self.nums.pop()
        return True



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums))]