# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

# 子数组 定义为原数组中的一个连续子序列。

# 请你返回 arr 中 所有奇数长度子数组的和 。

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        n = len(arr)
        m = n if n % 2 != 0 else n - 1
        for i in range(1, m + 1, 2):
            for j in range(0, n - i + 1):
                for k in range(j, j + i):
                    ans += arr[k]

        return ans 


arr = [1,4,2,5,3]

a = Solution()
print(a.sumOddLengthSubarrays(arr))