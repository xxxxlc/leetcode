# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

# 返回被除数 dividend 除以除数 divisor 得到的商。

# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

from turtle import right


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MIN = -2**31
        INI_MAX = 2**31 - 1

        if dividend == INT_MIN:
            if divisor == 1:
                return INT_MIN
            if divisor == -1:
                return INI_MAX
        
        if divisor == INT_MIN:
            return 1 if dividend == INT_MIN else 0
        if dividend == 0:
            return 0
        
        rev = False
        if dividend > 0:
            dividend = - dividend
            rev = not rev
        if divisor > 0:
            divisor = -divisor
            rev = not rev
        
        left, right, ans = 1, INI_MAX, 0

        while (left <= right):
            mid = left + ((right - left) >> 1)
            check = self.quickAdd(divisor, mid, dividend)

            if check:
                ans = mid
                if mid == INI_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        
        return -ans if rev else ans

    def quickAdd(self, y, z, x):
        result = 0
        add = y

        while z > 0:
            if (z & 1) == 1:
                if result < x - add:
                    return False
                result += add
            if z != 1:
                if add < x - add:
                    return False
                add += add
            z >>= 1
        return True

dividend = 1
divisor = 1

a = Solution()
print(a.divide(dividend, divisor))