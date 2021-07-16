# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        track = []
        self.backtrack(n, n, track)
        return self.res
    
    def backtrack(self, left, right, track):
        if right < left:
            return 
        if left < 0 or right < 0:
            return
        
        if left == 0 and right == 0:
            self.res.append("".join(track[:]))
            return
        
        track.append('(')
        self.backtrack(left - 1, right, track)
        track.pop(-1)

        track.append(')')
        self.backtrack(left, right - 1, track)
        track.pop(-1)


n = 3
a = Solution()
print(a.generateParenthesis(n))
