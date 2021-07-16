# 给定一个二叉树，在树的最后一行找到最左边的值。

import Bintree

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None
        
        q = []
        q.append(root)
        while(q):
            size = len(q)
            res = q[0].val
            for i in range(0, size):
                cur = q.pop(0)

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
        
        return res

root = [2,1,3]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.findBottomLeftValue(tree.root))