# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

# 提醒一下，二叉搜索树满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

import Bintree

class Solution(object):
    sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum = 0
        return self.helper(root)
        
    
    def helper(self, root):
        if root == None:
            return None
        
        self.helper(root.right)
        self.sum += root.val
        root.val = self.sum
        self.helper(root.left)

        return root


root = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
root = a.convertBST(tree.root)
tree.horizontallyshow(root, root)