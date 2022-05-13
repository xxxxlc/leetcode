# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。

# 例如，"ACGAATTCCG" 是一个 DNA序列 。
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。

# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        m = set()
        ans = set()

        for i in range(len(s) - 9):
            if s[i:i+10] not in m:
                m.add(s[i:i+10])
            else:
                ans.add(s[i:i+10])
        
        return list(ans)


s = "AAAAAAAAAAA"

a = Solution()
print(a.findRepeatedDnaSequences(s))