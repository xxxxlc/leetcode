# 给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

import Bintree
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        depth = 0
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
            
            depth += 1
        
        return pow(2, depth-1) - 1 + size

root = [1]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.countNodes(tree.root)) 
