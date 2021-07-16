# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        res = []
        need = dict()
        window = dict()

        for c in p:
            need[c] = need.get(c, 0) + 1
        
        left = right = 0
        vaild = 0
        
        while(right < len(s)):
            c = s[right]
            right += 1
            if c in need.keys():
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
            
            while(right - left >= len(p)):
                if vaild == len(need):
                    res.append(left)
                
                d = s[left]
                left += 1

                if d in need.keys():
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
        
        return res




s =  "cbaebabacd"
p =  "abc"
a = Solution()
print(a.findAnagrams(s, p))