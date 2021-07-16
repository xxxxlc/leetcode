# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。

# 返回移除了所有不包含 1 的子树的原二叉树


import Bintree

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and root.left == None and root.right == None:
            root = None
        
        return root



root = [1,None,0,0,1]
tree = Bintree.BinTree()
tree.CreateTree(root)

tree.horizontallyshow(tree.root, tree.root)

a = Solution()
root = a.pruneTree(tree.root)
tree.horizontallyshow(root, root)