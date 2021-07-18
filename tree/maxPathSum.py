# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

import Bintree

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('-inf')
        self.helper(root)

        return self.ans

    def helper(self, root):
        if root == None:
            return 0
        
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)

        val = left + right + root.val

        self.ans = max(self.ans, val)

        return max(left, right) + root.val
        

root = [9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6]

tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.maxPathSum(tree.root))