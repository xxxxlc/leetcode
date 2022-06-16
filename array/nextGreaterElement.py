# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))

        i = len(s) - 2
        while(i >= 0 and s[i + 1] <= s[i]):
            i = i - 1
        if i < 0:
            return -1
        
        j = len(s) - 1
        while (j >= 0 and s[j] <= s[i]):
            j = j - 1
        
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

        s[i+1:] = reversed(s[i+1:])

        ans = int("".join(s))
        if ans > 2**31 - 1:
            return -1
        else:
            return ans
        


n = 2147483486

a = Solution()
print(a.nextGreaterElement(n))