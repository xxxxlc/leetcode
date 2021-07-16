# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def f(root, res):
            if root == None:
                return res
            
            res.append(root.val)
            res = f(root.left, res)
            res = f(root.right, res)

            return res
        
        return f(root, res)