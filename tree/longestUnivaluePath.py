# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

# 注意：两个节点之间的路径长度由它们之间的边数表示。

import Bintree

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.helper(root)

        return self.ans

    
    def helper(self, root):
        if root == None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        root_length = 1
        l = r = 1
        if root.left and root.val == root.left.val:
            root_length += left
            l = left + 1
        if root.right and root.val == root.right.val:
            root_length += right
            r = right + 1
        
        if root_length > self.ans:
            self.ans = root_length-1
        
        return max(l, r)


        

root = [4,4,4,5,4,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.longestUnivaluePath(tree.root))