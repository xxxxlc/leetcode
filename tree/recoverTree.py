# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

import Bintree
from Bintree import TreeNode

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None

        pre = TreeNode(float("inf"))

        stack = []

        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                secondNode = p
            
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val


root = [1,3,None,None,2]

tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
root = a.recoverTree(tree.root)
tree.horizontallyshow(root, root)