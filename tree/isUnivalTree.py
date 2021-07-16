# 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

# 只有给定的树是单值二叉树时，才返回 true；否则返回 false。


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root, val):
            if root == None:
                return True
            
            if root.val != val:
                return False

            return f(root.left, val) and f(root.right, val)
        
        return f(root, root.val)


            
