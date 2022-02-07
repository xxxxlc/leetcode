# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

# 给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

# s 是一个尽可能长的快乐字符串。
# s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
# s 中只含有 'a'、'b' 、'c' 三种字母。
# 如果不存在这样的字符串 s ，请返回一个空字符串 ""。

# class Solution(object):
#     def longestDiverseString(self, a, b, c):
#         """
#         :type a: int
#         :type b: int
#         :type c: int
#         :rtype: str
#         """
#         self.ans = ""
#         self.maxlength = a + b + c
#         self.backtrack(a, b, c, "")
#         return self.ans
    
#     def backtrack(self, a, b, c, track):
#         if 'aaa' in track or 'bbb' in track or 'ccc' in track:
#             return
        
#         if len(self.ans) == self.maxlength:
#             return
#         if len(track) > len(self.ans):
#             self.ans = track

#         if a == 0 and b == 0 and c == 0:
#             self.ans = track
#             return

#         if a > 0:
#             self.backtrack(a - 1, b, c, track + 'a')
#         if b > 0:
#             self.backtrack(a, b - 1, c, track + 'b')
#         if c > 0:
#             self.backtrack(a, b, c - 1, track + 'c')


class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        ans = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]

        while True:
            cnt.sort(key=lambda x:-x[0])
            hasNext = False
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                    continue
                hasNext = True
                ans.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(ans)
a = 1
b = 1
c = 7

s = Solution()
print(s.longestDiverseString(a, b, c))