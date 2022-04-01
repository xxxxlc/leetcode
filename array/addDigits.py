# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        while (True):
            while (num != 0):
                ans += num % 10
                num = num // 10
            
            if ans // 10 == 0:
                break
            num = ans
            ans = 0
        return ans
    

num = 38

a = Solution()
print(a.addDigits(num))