# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果

class UnionFind:
    def __init__(self):
        self.father = {}
        self.weights = {} # 节点到父节点的权重
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.weights[x] = 1
    
    def find(self, x):# 查询根节点的同时进行路径压缩并修改权重
        root = x 
        while self.father[root] != None:
            root = self.father[root]
        # root为当前的根节点
        # 路径压缩并修改权重：迭代 改为 递归
        if x != root:
            original_father = self.father[x]
            root = self.find(original_father)
            self.father[x] = root
            self.weights[x] = self.weights[x] * self.weights[original_father]

        return root

    def merge(self, x, y, value):
        # value 为 x/y的值
        root_x, root_y = self.find(x), self.find(y)# 此处进行了查找，weights已经改变了
        if root_x != root_y:
            self.father[root_x] = root_y
            self.weights[root_x] = self.weights[y] * value / self.weights[x]


    def is_connected(self, x, y):
        # 判断xy是否在一个集合中，如果在一个集合中则返回除法的结果否则返回-1
        root_x ,root_y = self.find(x), self.find(y) # 注意此处执行了查询，修改了权重
        if root_x != root_y: # 不在一个集合中
            return -1
        return self.weights[x] / self.weights[y]
        


class Solution:
    def calcEquation(self, equations, values, queries):
        ans = []
        uf = UnionFind()
        # 根据equations 建立df
        for i, eq in enumerate(equations):
            uf.add(eq[0])
            uf.add(eq[1])
            uf.merge(eq[0], eq[1], values[i])
        # print(uf.father, uf.weights)
        # 查询uf
        for query in queries:
            x,y = query
            if x not in uf.father or y not in uf.father:
                ans.append(-1)
            else:
                ans.append(uf.is_connected(x, y))
        # print(uf.father, uf.weights)
        return ans



equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

a = Solution()
print(a.calcEquation(equations, values, queries))

