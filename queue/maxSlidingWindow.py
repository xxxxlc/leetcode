# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。

class  MonotonicQueue(object):
    def __init__(self):
        self.q = []

    def push(self, n: int):
        while(self.q and n > self.q[len(self.q) - 1]):
            self.q.pop(len(self.q) - 1)
        
        self.q.append(n)
    
    def max(self):
        return self.q[0]
    
    def pop(self, n):
        if n == self.q[0]:
            self.q.pop(0)
    
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = MonotonicQueue()
        i = 0
        while(i < len(nums)):
            while (i < k - 1):
                q.push(nums[i])
                i += 1
            
            q.push(nums[i])
            res.append(q.max())
            i = i + 1
            q.pop(nums[i - k])
            
        return res
            
            



nums = [1,-1]
k = 1

a = Solution()
print(a.maxSlidingWindow(nums, k))