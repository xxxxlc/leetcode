# 给你两个下标从 0 开始的字符串 word1 和 word2 。

# 一次 移动 由以下两个步骤组成：

# 选中两个下标 i 和 j ，分别满足 0 <= i < word1.length 和 0 <= j < word2.length ，
# 交换 word1[i] 和 word2[j] 。
# 如果可以通过 恰好一次 移动，使 word1 和 word2 中不同字符的数目相等，则返回 true ；否则，返回 false 

from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        word1 = Counter(word1)
        word2 = Counter(word2)

        for x, c in word1.items():
            for y, d in word2.items():
                if x == y:
                    if len(word1) == len(word2):
                        return True
                elif len(word1) - (c == 1) + (y not in word1) == len(word2) - (d == 1) + (x not in word2):
                    return True

        return False





word1 = "ac"
word2 = "b"

a = Solution()
print(a.isItPossible(word1, word2))