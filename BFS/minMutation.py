# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

# 假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

# 例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

# 与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

# 现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

# 注意：

# 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
# 如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
# 假定起始基因序列与目标基因序列是不一样的。

class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1

        gens = {"A", "C", "G", "T"}
        visited = {start}
        q = [start]
        depth = 0
        while q:
            size = len(q)

            for _ in range(size):
                cur = q.pop(0)

                if cur == end:
                    return depth
                
                for j in range(len(cur)):
                    s = cur[:]
                    for gen in gens:
                        s = s[:j] + gen + s[j+1:]
                        if s not in visited and s in bank:
                            q.append(s)
                            visited.add(s)
            depth += 1
        
        return -1



start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]

a = Solution()
print(a.minMutation(start, end, bank))