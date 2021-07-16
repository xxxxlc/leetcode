# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

import Bintree

class Solution(object):
    minabs = float('inf')
    abs = None
    pre = None
    def update(self, x):
        if self.pre == None:
            self.pre = x
        else:
            self.abs = abs(self.pre - x)
            if self.abs < self.minabs:
                self.minabs = self.abs
            self.pre = x
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return
        self.getMinimumDifference(root.left)
        self.update(root.val)
        self.getMinimumDifference(root.right)

        return self.minabs
        
    
root = [1,None,2,3]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.getMinimumDifference(tree.root))