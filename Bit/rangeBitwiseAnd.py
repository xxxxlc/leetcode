# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        ans = 0

        while (left < right):
            left = left >> 1
            right = right >> 1
            ans += 1
        return right << ans

left = 5
right = 7

a = Solution()
print(a.rangeBitwiseAnd(left, right))