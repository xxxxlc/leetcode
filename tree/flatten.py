# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

import Bintree
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        res = []
        res = self.preorder(root, res)

        for i in range(1, len(res)):
            node = Bintree.TreeNode(res[i])
            root.left = None
            root.right = node
            root = root.right

    def preorder(self, root, res):
        if root == None:
            return res
        
        res.append(root.val)

        res = self.preorder(root.left, res)
        res = self.preorder(root.right, res)

        return res


root = [1,2,5,3,4,None,6]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
a.flatten(tree.root)
tree.horizontallyshow(tree.root, tree.root)