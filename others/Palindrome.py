# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

class Solution(object):
    def __init__(self):
        pass
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_number = str(x)
        if str_number == str_number[::-1]:
            return True
        else:
            return False

a = Solution()
print(a.isPalindrome(-121))