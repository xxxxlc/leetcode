# 给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。

# 你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：

# 从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。
# 返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。

# 注意：

# 查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。
# 树的高度是从根到树中某个节点的 最长简单路径中的边数 。



from collections import defaultdict


class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        height = defaultdict(int)

        def getHeight(node):
            if node is None: return 0
            height[node] = 1 + max(getHeight(node.left), getHeight(node.right))
            return height[node]
        
        getHeight(root)

        res = [0] * (len(height) + 1)

        def dfs(node, depth, rest_h):
            if node is None:
                return
            depth += 1
            res[node.val] = rest_h
            dfs(node.right, depth, max(rest_h, depth + height[node.left]))
            dfs(node.left, depth, max(rest_h, depth + height[node.right]))
        dfs(root, -1, 0)

        for i, q in enumerate(queries):
            queries[i] = res[q]
        return queries

