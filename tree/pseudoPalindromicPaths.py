# 给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

# 请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

import Bintree

class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.ans = 0
        nums = 0
        self.dfs(root, nums)
        return self.ans
    
    def dfs(self, root, temp):
        n = temp ^ (1 << root.val)
        if root.left == None and root.right == None:
            if n == 0 or n & (n - 1) == 0:
                self.ans += 1
        
        if root.left:
            self.dfs(root.left, n)
        
        if root.right:
            self.dfs(root.right, n)
        


root = [1,9,1,None,1,None,1,None,None,7,None,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.pseudoPalindromicPaths(tree.root))


