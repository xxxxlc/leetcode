# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

import Bintree

class Solution(object):
    ans = Bintree.TreeNode()
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.bfs(root, p, q)
        return self.ans
    
    def bfs(self, root, p ,q):
        if root == None:
            return False
        left = self.bfs(root.left, p, q)
        right = self.bfs(root.right, p, q)

        if ((left and right) or ((root.val == p.val) or (root.val == q.val) and (left or right))):
            self.ans = root
        
        return left or right or (root.val == p.val) or (root.val == q.val)





    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res = []
        res_p = []
        res_q = []

        def f(root, res, p, q, res_p, res_q):
            if root == None:
                return res_p, res_q
            if root.val == p:
                res_p = res[:]
            if root.val == q:
                res_q = res[:]
            if root.left == None and root.right == None:
                res.append(root.val)
                #print(res)
                res.pop()
                return res_p, res_q
            
            
            res.append(root.val)
            res_p, res_q = f(root.left, res, p, q, res_p, res_q)
            res_p, res_q = f(root.right, res, p, q, res_p, res_q)
            res.pop()

            return res_p, res_q

        res_p, res_q = f(root, res, p, q, res_p, res_q)

        for i in range(0, len(res_q)):
            for j in range(0, len(res_p)):
                if res_q[len(res_q) - 1 - i] == res_p[j]:
                    return res_p[j]



# root = [3,5,1,6,2,0,8,None,None,7,4]
root = [-1,0,3,-2,4,None,None,8]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
p = 8
q = 4
print(a.lowestCommonAncestor(tree.root, p, q))