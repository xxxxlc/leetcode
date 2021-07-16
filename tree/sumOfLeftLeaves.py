# 计算给定二叉树的所有左叶子之和。

import Bintree

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def f(root, sumleft):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 0
            if root.left == None and root.right != None:
                return f(root.right, sumleft)
            if root.left.left == None and root.left.right == None:
                return root.left.val + f(root.right, sumleft)
            
            sumleft_left = sumleft + f(root.left, sumleft)
            sumleft_right = sumleft + f(root.right, sumleft)
            return sumleft_left + sumleft_right


        return f(root, 0)

    
    def sumOfLeftLeaves_1(self, root):
        if root == None:
            return 0
        return (self.sumOfLeftLeaves_1(root.left) + self.sumOfLeftLeaves_1(root.right) + 
        (root.left.val if root.left != None and root.left.left == None and root.left.right == None else 0))



# root = [1,2,4,1,None,3,-1,5,1,None,6,None,8]
root = [3,9,20,None,None,15,7]
tree = Bintree.BinTree()
tree.CreateTree(root)
# tree.preOrderTraversal(tree.root)

a = Solution()
print(a.sumOfLeftLeaves(tree.root))
print(a.sumOfLeftLeaves_1(tree.root))