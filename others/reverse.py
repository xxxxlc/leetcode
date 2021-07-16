# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number_string = str(x)
        number_string = number_string[::-1]
        if x >= 0:
            result =  int(number_string)
        else:
            result =  -int(number_string[0:len(number_string)-1])
        if result >= pow(2,31) - 1 or result <= -pow(2,31):
            return 0
        else:
            return result

a = Solution()
x = 123
print(a.reverse(x))