# 给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

# 由于答案可能很大，因此 返回答案模 10^9 + 7 。


class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        monoStack = []

        dp = [0] * n
        ans = 0

        for i, x in enumerate(arr):
            while monoStack and arr[monoStack[-1]] > x:
                monoStack.pop()
            k = i - monoStack[-1] if monoStack else i + 1
            dp[i] = k * x + (dp[i - k] if monoStack else 0)
            ans = (ans + dp[i]) % (1e9 + 7)
            monoStack.append(i)
        return ans


arr = [11,81,94,43,3]
a = Solution()
print(a.sumSubarrayMins(arr))