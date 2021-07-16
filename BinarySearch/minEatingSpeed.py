# 珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

# 珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

# 珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

# 返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles) + 1
        while(left < right):
            mid = left + (right - left) // 2
            if self.can(mid, piles, h):
                right = mid
            else:
                left = mid+1 
        return left
    
    def can(self, mid, piles, h):
        time = 0
        for i in range(0, len(piles)):
            time += self.timeof(mid, piles[i])

        return time <= h
    
    def timeof(self, mid, x):
        return x//mid + (x % mid > 0)


a = Solution()
piles = [3,6,7,11]
h = 8
print(a.minEatingSpeed(piles, h))