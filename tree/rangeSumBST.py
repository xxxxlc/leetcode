# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

import  Bintree
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        sum_bst = 0
        sum_bst = self.sum_bst_range(root, low, high, sum_bst)
        return sum_bst

    def sum_bst_range(self, root, low, high, sum_bst):
        if root == None:
            return 0

        if root.val > high or root.val < low:
            return self.sum_bst_range(root.left, low, high, sum_bst) + self.sum_bst_range(root.right, low, high, sum_bst)

        return root.val + self.sum_bst_range(root.left, low, high, sum_bst) + self.sum_bst_range(root.right, low, high, sum_bst)


root = [10,5,15,3,7,None,18]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
low = 7
high = 15
print(a.rangeSumBST(tree.root, low, high))