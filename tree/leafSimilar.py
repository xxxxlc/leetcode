# 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 

import Bintree

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf1 = []
        leaf2 = []


        leaf1 = self.findleaf(root1, leaf1)
        leaf2 = self.findleaf(root2, leaf2)
        if leaf1 == leaf2:
            return True
        
        return False
    
    def findleaf(self, root, leaf):
        if root == None:
            return []
        
        self.findleaf(root.left, leaf)
        if root.left == None and root.right == None:
            leaf.append(root.val)
        self.findleaf(root.right, leaf)

        return leaf
        

root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
tree1 = Bintree.BinTree()
tree2 = Bintree.BinTree()
tree1.CreateTree(root1)
tree2.CreateTree(root2)

a = Solution()
print(a.leafSimilar(tree1.root, tree2.root))