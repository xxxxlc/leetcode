# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        need = dict()
        window = dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
        left = right = 0
        start = 0
        length = float('inf')
        vaild = 0
        while(right < len(s)):
            c = s[right]
            right += 1

            if c in need.keys():
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
            
            while(vaild == len(need)):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1
                if d in need.keys():
                    if need[d] == window[d]:
                        vaild -= 1
                    window[d] -= 1
                    
        if length == float('inf'):
            return ""
        return s[start:start + length]



a = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(a.minWindow(s, t))