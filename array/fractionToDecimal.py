# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以 字符串形式返回小数 。

# 如果小数部分为循环小数，则将循环的部分括在括号内。

# 如果存在多个答案，只需返回 任意一个 。

# 对于所有给定的输入，保证 答案字符串的长度小于 104 。

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        s = []

        if (numerator < 0) != (denominator < 0):
            s.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)
        integerPart = numerator // denominator
        s.append((str(integerPart)))
        s.append('.')

        indexMap = {}
        remainder = numerator % denominator

        while(remainder and remainder not in indexMap):
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder // denominator))
            remainder %= denominator
        if remainder:
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')
        return "".join(s)            

numerator = 4
denominator = 333

a = Solution()
print(a.fractionToDecimal(numerator, denominator))