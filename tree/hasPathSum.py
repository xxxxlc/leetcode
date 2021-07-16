# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
import Bintree

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        if root.left == None and root.right == None:
            return sum == root.val
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

a = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = Bintree.BinTree()
tree.CreateTree(a)
#tree.preOrderTraversal(tree.root)
b = Solution()
print(b.hasPathSum(tree.root, 22))