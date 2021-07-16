# 给定一个 N 叉树，找到其最大深度。

# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
        for children in root.children:
            H = self.maxDepth(children)
            if H > depth:
                depth = H

        return depth + 1

        