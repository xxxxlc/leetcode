# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        stack = [-1]

        i = 0
        ans = 0
        temp = 0
        while(i < len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    temp = i - stack[-1]
                    if temp > ans:
                        ans = temp
            i = i + 1
        return ans


s = "))()())"

a = Solution()
print(a.longestValidParentheses(s))