# 传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

# 传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

# 返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights) + 1
        while(left < right):
            mid = left + (right - left) // 2
            if self.can(mid, weights, D):
                right = mid
            else:
                left = mid + 1
        
        
        return left

    def can(self, mid, weights, D):
        day = 1
        i = 0
        temp = 0
        while(i < len(weights)):
            temp += weights[i]
            if temp > mid:
                temp = weights[i]
                day += 1
            i += 1
        
        return day <= D




a = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(a.shipWithinDays(weights, D))