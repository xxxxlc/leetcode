# 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

# （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

import Bintree

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        maxval = float('-inf')
        minval = float('inf')
        return self.helper(root, maxval, minval, 0)
    
    def helper(self, root, maxval, minval, diff):
        if root == None:
            return 0
        
        if root.val < minval:
            minval = root.val
        
        if root.val > maxval:
            maxval = root.val

        if diff < maxval - minval:
            diff = maxval - minval
        
        left = self.helper(root.left, maxval, minval, diff)
        right =  self.helper(root.right, maxval, minval, diff)

        return max(left, right, diff)


root = [8,3,10,1,6,None,14,None,None,4,7,13]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.maxAncestorDiff(tree.root))