# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

import Bintree
class Solution(object):
    def rightSideView(self, root):
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
            for i in range(0, size):
                cur = q.pop(0)
            
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)

                if i == size - 1:
                    res.append(cur.val)
        
        return res


root = [1,2,3,None,5,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.rightSideView(tree.root))
