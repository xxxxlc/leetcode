# 对任一由 n 个小写英文字母组成的字符串 word ，我们可以定义一个 n x n 的矩阵，并满足：

# lcp[i][j] 等于子字符串 word[i,...,n-1] 和 word[j,...,n-1] 之间的最长公共前缀的长度。
# 给你一个 n x n 的矩阵 lcp 。返回与 lcp 对应的、按字典序最小的字符串 word 。如果不存在这样的字符串，则返回空字符串。

# 对于长度相同的两个字符串 a 和 b ，如果在 a 和 b 不同的第一个位置，字符串 a 的字母在字母表中出现的顺序先于 b 中的对应字母，则认为字符串 a 按字典序比字符串 b 小。例如，"aabd" 在字典上小于 "aaca" ，因为二者不同的第一位置是第三个字母，而 'b' 先于 'c' 出现。

from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:


lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]

a = Solution()
print(a.findTheString(lcp))