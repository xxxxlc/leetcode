# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

# 进阶：不要 使用任何内置的库函数，如  sqrt 。




class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num

        while (left <= right):
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

num = 14
a = Solution()
print(a.isPerfectSquare(num))