# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        path = dict()
        def dp(i ,j):
            if (i ,j) in path:
                return path[(i, j)]
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                path[(i, j)] = dp(i - 1, j - 1)
                return path[(i ,j)]
            else:
                path[(i, j)] = min(
                    dp(i, j - 1) + 1,
                    dp(i - 1 , j) + 1,
                    dp(i - 1 , j - 1) + 1
                )
                return path[(i,j)]
        
        return dp(len(word1)-1, len(word2)-1)



word1 = 'rad'
word2 = 'apple'
a = Solution()
print(a.minDistance(word1, word2))