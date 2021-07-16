# 给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

# 选择二叉树中 任意 节点和一个方向（左或者右）。
# 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
# 改变前进方向：左变右或者右变左。
# 重复第二步和第三步，直到你在树中无法继续移动。
# 交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

# 请你返回给定树中最长 交错路径 的长度。

import Bintree

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.maxlength = 0
        length = 0
        self.helper(root.left, length + 1, 1)
        self.helper(root.right, length + 1, -1)
        return self.maxlength
    
    def helper(self, root, length, way):


        if root == None:
            return length

        if length > self.maxlength:
            self.maxlength = length

        if way == 1:
            self.helper(root.left, 1, 1)
            self.helper(root.right, length + 1, -1)
        
        elif way == -1:
            self.helper(root.left, length + 1, 1)
            self.helper(root.right, 1, -1)
        



root = [1,None,1,1,1,None,None,1,1,None,1,None,None,None,1,None,1]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.longestZigZag(tree.root))

