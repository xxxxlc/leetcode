# 给你两棵二叉树，原始树 original 和克隆树 cloned，以及一个位于原始树 original 中的目标节点 target。

# 其中，克隆树 cloned 是原始树 original 的一个 副本 。

# 请找出在树 cloned 中，与 target 相同 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。

import Bintree

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        self.ans = None
        self.helper(original, cloned, target)
        return self.ans
    
    def helper(self, original, cloned, target):
        if original == None:
            return
        
        if original == target:
            self.ans = cloned
            return
        
        self.helper(original.left, cloned.left, target)
        self.helper(original.right, cloned.right, target)

root = [7,4,3,None,None,6,19]
target = 3
tree1 = Bintree.BinTree()
tree2 = Bintree.BinTree()
tree1.CreateTree(root)
tree2.CreateTree(root)

a = Solution()
ans = a.getTargetCopy(tree1, tree2, target)