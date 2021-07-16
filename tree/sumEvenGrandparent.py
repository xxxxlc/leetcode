# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

# 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
# 如果不存在祖父节点值为偶数的节点，那么返回 0 。

import Bintree

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        res = 0
        q = []
        q.append(root)
        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)
                if cur.val % 2 == 0:
                    res += self.helper(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return res
    
    def helper(self, root):
        q = []
        q.append(root)
        for i in range(0, 2):
            for j in range(0, len(q)):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return sum([node.val for node in q])


root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.sumEvenGrandparent(tree.root))