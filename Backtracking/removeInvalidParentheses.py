# 给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

# 返回所有可能的结果。答案可以按 任意顺序 返回。

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.stack = []
        self.res = []

        lremove = 0
        rremove = 0

        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1
        self.backtrack(0, s, lremove, rremove)
        return self.res

    def backtrack(self, idx, s, lremove, rremove):

        if lremove == 0 and rremove == 0:
            if self.isVaild(s):
                self.res.append(s[:])
            return
        
        for i in range(idx, len(s)):
            if i > idx and s[i] == s[i - 1]:
                continue
            if lremove + rremove > len(s) - i:
                break

            if lremove > 0 and s[i] == '(':
                self.backtrack(i, s[:i] + s[i + 1:], lremove - 1, rremove)
            if rremove > 0 and s[i] == ')':
                self.backtrack(i, s[:i] + s[i + 1:], lremove, rremove - 1)
    
    
    def isVaild(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
                if cnt < 0:
                    return False

        return cnt == 0
            




s = "()())()"

a = Solution()
print(a.removeInvalidParentheses(s))