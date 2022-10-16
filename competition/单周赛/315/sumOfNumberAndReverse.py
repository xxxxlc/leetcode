# 给你一个 非负 整数 num 。如果存在某个 非负 整数 k 满足 k + reverse(k) = num  ，则返回 true ；否则，返回 false 。

# reverse(k) 表示 k 反转每个数位后得到的数字。

class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num // 2, num):
            if i + self.reverse(i) == num:
                return True
        
        return False

    def reverse(self, num):
        s = str(num)[::-1]
        num = int(s)
        return num

num = 443

a = Solution()
print(a.sumOfNumberAndReverse(num))