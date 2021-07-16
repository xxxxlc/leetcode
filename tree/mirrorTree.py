# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

import Bintree
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        temp = Bintree.TreeNode()
        temp = root.left
        root.left = root.right
        root.right = temp

        return root



node = [4,2,7,1,3,6,9]
tree = Bintree.BinTree()
tree.CreateTree(node)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
root = a.mirrorTree(tree.root)
tree.horizontallyshow(root, root)