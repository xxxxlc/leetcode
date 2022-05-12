# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

num1 = "2"
num2 = "3"

a = Solution()
print(a.multiply(num1, num2))