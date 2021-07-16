# 您需要在二叉树的每一行中找到最大的值。

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        q = []
        q.append(root)

        while(q):
            size = len(q)
            max_depth = float('-inf')
            for i in range(0, size):
                cur = q.pop(0)
                if cur.val > max_depth:
                    max_depth = cur.val
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
            
            res.append(max_depth)
        
        return res