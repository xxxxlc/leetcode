# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。
# 你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """

        res = self.helper(expression)
        return list(res)
        

    def helper(self, input):
        res = []
        for i in range(0, len(input)):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                left = self.helper(input[:i])
                right = self.helper(input[i+1:])
                for a in left:
                    for b in right:
                        if c == '+':
                            res.append(a + b)
                        elif c == '-':
                            res.append(a - b)
                        elif c == '*':
                            res.append(a * b)
        
        if len(res) == 0:
            return [int(input)]
        return res


expression = '2*3-4*5'
a = Solution()
print(a.diffWaysToCompute(expression))
