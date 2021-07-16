# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

# 「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

import Bintree

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helper(root, root.val)
    
    def helper(self, root, max):
        if root == None:
            return 0

        if root.val >= max:
            return 1 + self.helper(root.left, root.val) + self.helper(root.right, root.val)
        return self.helper(root.left, max) + self.helper(root.right, max)
        


root = [3,1,4,3,None,1,5]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.goodNodes(tree.root))