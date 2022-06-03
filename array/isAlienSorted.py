# 某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。

# 给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        if len(words) == 1:
            return True

        return all(self.isafter(words[i], words[i + 1], order) for i in range(len(words) - 1))
    
    def isafter(self, s1, s2, order):

        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                continue
            else:
                return order.index(s1[i]) < order.index(s2[i])
        if len(s1) <= len(s2):
            return True
        else:
            return False





words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

a = Solution()
print(a.isAlienSorted(words, order))
