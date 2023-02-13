# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。

# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^ firsti == secondi 。

# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 lefti 最小的一个。

# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。

# 子字符串 是一个字符串中一段连续非空的字符序列。

from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        m = {}

        for l in range(n):
            x = 0
            for r in range(l, min(n, l + 30)):
                x = (x << 1) | ord(s[r]) & 1

                if x not in m or r-l < m[x][1] - m[x][0]:
                    m[x] = (l, r)
        
        NOT_FOUND = (-1, -1)

        return [m.get(x ^ y, NOT_FOUND) for x, y in queries]
        




s = "101101"
queries = [[0,5],[1,2]]

a = Solution()
print(a.substringXorQueries(s, queries))
