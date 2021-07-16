# 给你一棵以 root 为根的二叉树和一个整数 target ，请你删除所有值为 target 的 叶子节点 。

# 注意，一旦删除值为 target 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 target ，那么这个节点也应该被删除。

# 也就是说，你需要重复此过程直到不能继续删除

import Bintree
from Bintree import TreeNode

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.left == None and root.right == None and root.val == target:
            root = None

        return root


root = [1,2,3,2,None,2,4]
target = 2

tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
root = a.removeLeafNodes(tree.root, target)
tree.horizontallyshow(root, root)