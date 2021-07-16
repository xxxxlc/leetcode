# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        if s == '':
            return 0
        for i in range(len(s) - 1):
            num += dict_roman[s[i]]
            if dict_roman[s[i]] < dict_roman[s[i+1]]:
                num = num - 2*dict_roman[s[i]]
        num = num + dict_roman[s[len(s) - 1]]
        
        return num



a = Solution()
input = 'XXVII'
print(a.romanToInt(input))