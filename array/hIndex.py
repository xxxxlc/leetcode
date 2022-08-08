# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

# 根据维基百科上 h 指数的定义：h 代表“高引用次数”，一名科研人员的 h指数是指他（她）的 （n 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 n - h 篇论文每篇被引用次数 不超过 h 次。

# 如果 h 有多种可能的值，h 指数 是其中最大的那个。

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        
        for i in range(len(citations)):
            h_index = len(citations) - i
            if citations[i] >= h_index:
                return h_index
        
        return 0


citations = [1,3,1]

a = Solution()
print(a.hIndex(citations))