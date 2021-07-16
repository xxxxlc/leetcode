import Bintree

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return

        # temp = Bintree.TreeNode()
        # temp = root.left
        # root.left = root.right
        # root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = Bintree.TreeNode()
        temp = root.left
        root.left = root.right
        root.right = temp

        return root

a = [4,2,7,1,3,6,9]
tree = Bintree.BinTree()
tree.CreateTree(a)
# print(tree.preOrderTraversal(tree.root))

b = Solution()
tree.preOrderTraversal(b.invertTree(tree.root))