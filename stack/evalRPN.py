# 根据 逆波兰表示法，求表达式的值。

# 有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 注意 两个整数之间的除法只保留整数部分。

# 可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """


        stack = []

        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    num = num1 + num2
                elif token == '-':
                    num = num1 - num2
                elif token == "*":
                    num = num1 * num2
                else:
                    num = int(num1 / num2)
            finally:
                stack.append(num)
        
        return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

a = Solution()
print(a.evalRPN(tokens))