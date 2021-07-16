# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

import Bintree
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if not root1:
            return root2
        
        if not root2:
            return root1

        root1.val = root1.val + root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1





root1 = [1,3,2,5]
tree1 = Bintree.BinTree()
tree1.CreateTree(root1)
tree1.horizontallyshow(tree1.root, tree1.root)

root2 = [2,1,3,None,4,7]
tree2 = Bintree.BinTree()
tree2.CreateTree(root2)
tree2.horizontallyshow(tree2.root, tree2.root)


a = Solution()
root = a.mergeTrees(tree1.root, tree2.root)
tree1.horizontallyshow(root, root)