# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))

num1 = "11"
num2 = "123"

a = Solution()
print(a.addStrings(num1, num2))