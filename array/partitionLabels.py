# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        A = [0] * 26

        for i, ch in enumerate(s):
            A[ord(ch) - ord("a")] = i
        
        partition = list()
        end = start = 0
        for i, ch in enumerate(s):
            end = max(end, A[ord(ch) - ord("a")])
            if i == end:
                partition.append(end - start + 1)
                start = end + 1
        return partition

S = "ababcbacadefegdehijhklij"
a = Solution()
print(a.partitionLabels(S))