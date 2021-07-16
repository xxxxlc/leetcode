# 给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

# 由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

import Bintree

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return
        self.res = 0
        all = self.helper1(root)
        self.helper2(root, all)
        # print(all)
        return self.res % (10**9 + 7)

    def helper1(self, root):
        if root == None:
            return 0
        
        return root.val + self.helper1(root.left) + self.helper1(root.right)

    def helper2(self, root, all):
        if root == None:
            return 0
        
        left = self.helper2(root.left, all)
        right = self.helper2(root.right, all)

        self.res = max(self.res, left * (all - left), right * (all - right))

        return root.val + left + right


root = [1,None,2,3,4,None,None,5,6]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.maxProduct(tree.root))