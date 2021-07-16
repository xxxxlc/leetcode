# 给定一个二叉树，找出其最大深度。

# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        HL = self.maxDepth(root.left)
        HR = self.maxDepth(root.right)

        if HL > HR:
            return HL + 1
        else:
            return HR + 1