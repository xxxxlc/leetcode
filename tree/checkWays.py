# 给你一个数组 pairs ，其中 pairs[i] = [xi, yi] ，并且满足：

# pairs 中没有重复元素
# xi < yi
# 令 ways 为满足下面条件的有根树的方案数：

# 树所包含的所有节点值都在 pairs 中。
# 一个数对 [xi, yi] 出现在 pairs 中 当且仅当 xi 是 yi 的祖先或者 yi 是 xi 的祖先。
# 注意：构造出来的树不一定是二叉树。
# 两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。

# 请你返回：

# 如果 ways == 0 ，返回 0 。
# 如果 ways == 1 ，返回 1 。
# 如果 ways > 1 ，返回 2 。
# 一棵 有根树 指的是只有一个根节点的树，所有边都是从根往外的方向。

# 我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 祖先 。根节点没有祖先。


from collections import defaultdict
from email.policy import default
from platform import node
from sys import maxsize

from sklearn import neighbors


class Solution(object):
    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(set)

        for x, y in pairs:
            adj[x].add(y)
            adj[y].add(x)
        
        root = next((node for node, neighbours in adj.items() if len(neighbours) == len(adj) - 1), -1)
        if root == -1:
            return 0
        
        ans = 1

        for ndoe, neighbors in adj.items():
            if node == root:
                continue

            currDegree = len(neighbors)
            parent = -1
            parentDegree = maxsize

            for neighbor in neighbors:
                if currDegree <= len(adj[neighbor]) < parentDegree:
                    parent = neighbor
                    parentDegree = len(adj[neighbor])
            
            if parent == -1 or any(neighbor != parent and neighbor not in adj[parent] for neighbor in neighbors):
                return 0
            
            if parentDegree == currDegree:
                ans = 2
        return ans

