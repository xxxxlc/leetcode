# 给你一个整数 n，请你帮忙统计一下我们可以按下述规则形成多少个长度为 n 的字符串：

# 字符串中的每个字符都应当是小写元音字母（'a', 'e', 'i', 'o', 'u'）
# 每个元音 'a' 后面都只能跟着 'e'
# 每个元音 'e' 后面只能跟着 'a' 或者是 'i'
# 每个元音 'i' 后面 不能 再跟着另一个 'i'
# 每个元音 'o' 后面只能跟着 'i' 或者是 'u'
# 每个元音 'u' 后面只能跟着 'a'
# 由于答案可能会很大，所以请你返回 模 10^9 + 7 之后的结果

class Solution1(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = []
        self.size = n
        track = []
        char = ['a','e','i','o','u']
        self.backtrack(track, char)
        return len(self.res) % (10 ** 9 + 7)
    
    def backtrack(self, track, char):
        if len(track) == self.size:
            self.res.append(track[:])
            return

        for c in char:
            if not track:
                track.append(c)
                self.backtrack(track, char)
                track.pop(-1)
                continue
            
            if self.rule(c, track[-1]):
                track.append(c)
                self.backtrack(track, char)
                track.pop(-1)
            else:
                continue
    
    def rule(self, c, a):
        if a == 'a' and c != 'e':
            return False
        elif (a == 'e' and c != 'i') and (a == 'e' and c != 'a'):
            return False 
        elif a == 'i' and c == 'i':
            return False
        elif (a == 'o' and c != 'i') and (a == 'o' and c != 'u'):
            return False
        elif a == 'u' and c != 'a':
            return False
        else:
            return True
        
    

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007


a = Solution()
n = 5
print(a.countVowelPermutation(n))
