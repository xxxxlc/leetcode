# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。

# 在执行上述操作后，返回包含相同字母的最长子字符串的长度。

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = [0] * 26
        left = right = maxn = 0
        n = len(s)

        while(right < n):
            num[ord(s[right]) - ord('A')] += 1
            maxn = max(maxn, num[ord(s[right]) - ord('A')])

            if right - left + 1 - maxn > k:
                num[ord(s[left]) - ord('A')] -= 1
                left += 1
            right += 1
        
        return right - left

s = "ABAB"
k = 2

a = Solution()
print(a.characterReplacement(s, k))