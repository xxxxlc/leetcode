# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            
            else:
                if len(stack) > 0:
                    s = stack.pop(-1)
                    if s == '(':
                        if c != ')':
                            return False
                    elif s == '[':
                        if c != ']':
                            return False
                    elif s == '{':
                        if c != '}':
                            return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True


s = "{{"

a = Solution()
print(a.isValid(s))


