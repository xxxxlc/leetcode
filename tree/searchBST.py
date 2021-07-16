# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

import Bintree

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)

        if left:
            return left
        elif right:
            return right
        else:
            return

root = [4,2,7,1,3]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
root = a.searchBST(tree.root, 5)
tree.horizontallyshow(root, root)