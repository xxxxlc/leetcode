# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

import Bintree

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        inorder = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= inorder:
                return False
            
            inorder = root.val
            root = root.right
        
        return True



            


root = [2,1,3]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.isValidBST(tree.root))


