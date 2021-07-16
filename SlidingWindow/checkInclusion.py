# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

# 换句话说，第一个字符串的排列之一是第二个字符串的 子串 。

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        need = dict()
        window = dict()

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = right = 0
        vaild = 0
        while(right < len(s2)):
            c = s2[right]
            right += 1
            if c in need.keys():
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    vaild += 1
                
            while(right - left >= len(s1)):
                if vaild == len(need):
                    return True
                
                d = s2[left]
                left += 1

                if d in need.keys():
                    if window[d] == need[d]:
                        vaild -= 1
                    window[d] -= 1
                
            # print(left, right)
            # print(s2[left:right])
            # for key,value in window.items():
            #     print(key, value)
            # print('\n')
            
        
        return False




s1 = "adc"

s2 = "dcda"
s1 = "hello"
s2 = "ooolleoooleh"
a = Solution()
print(a.checkInclusion(s1, s2))