# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []

        self.backtrack(s, '', 0)

        return self.ans
    
    def backtrack(self, s, track, idx):
        if len(track) == len(s):
            self.ans.append(track[:])
            return

        if s[idx].isdigit():
            self.backtrack(s, track + s[idx], idx + 1)
        else:
            self.backtrack(s, track + self.transfer(s[idx]), idx + 1)
            self.backtrack(s, track + s[idx], idx + 1)
            
    
    def transfer(self, c):
        if c.isdigit():
            return c
        if c.isupper():
            return chr(ord(c) + 32)
        else:
            return chr(ord(c) - 32)


s = "a1b2"

a = Solution()
print(a.letterCasePermutation(s))