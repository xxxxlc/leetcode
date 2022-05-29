# 给你一个数字数组 arr 。

# 如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

# 如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        min_element = min(arr)
        max_element = max(arr)
        n = len(arr)

        diff = (max_element - min_element) / float(n - 1)

        c = min_element
        for _ in range(1, n):
            c += diff
            if c not in arr:
                return False
        
        return True

arr = [0,0,1]

a = Solution()
print(a.canMakeArithmeticProgression(arr))