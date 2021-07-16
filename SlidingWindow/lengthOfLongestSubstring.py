# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        
        window = dict()
        length = 0
        left = right = 0
        while(right < len(s)):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while(window[c] > 1):
                d = s[left]
                window[d] -= 1
                left += 1
            
            if right - left > length:
                length = right - left
            
        return length


s = " "

a = Solution()
print(a.lengthOfLongestSubstring(s))