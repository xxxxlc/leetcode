# 给定一个正整数 n ，输出外观数列的第 n 项。

# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

# 你可以将其视作是由递归公式定义的数字字符串序列：

# countAndSay(1) = "1"
# countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

import collections

class Solution(object):
    t = {}
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n in self.t:
            return self.t[n]

        if n == 1:
            return "1"
        
        s = self.countAndSay(n - 1)

        j = 0
        c_num = 1
        ans = ""
        while (j < len(s)):
            if j + 1 < len(s) and s[j] == s[j + 1]:
                c_num += 1
                j += 1
                continue
            ans += str(c_num) + s[j]
            c_num = 1
            j += 1
        
        return ans


n = 5

a = Solution()
print(a.countAndSay(n))
