# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"

from re import S


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        s = 'balloon'
        balloon = dict()
        for c in s:
            balloon[c] = 0
        
        for c in text:
            if c in balloon.keys():
                balloon[c] += 1
        
        ans = float('inf')
        for key, value in balloon.items():
            if key == 'l' or key == 'o':
                temp = value // 2
            else:
                temp = value
            
            if temp < ans:
                ans = temp

        return ans 

text = "nlaebolko"

a = Solution()
print(a.maxNumberOfBalloons(text))