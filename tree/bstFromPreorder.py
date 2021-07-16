# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。

# (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right 的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）

# 题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。

import Bintree
from Bintree import TreeNode

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        i = 1
        while(i < len(preorder) and preorder[i] < preorder[0]):
            i += 1
        
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root

        

preorder = [4,2]
a = Solution()

root = a.bstFromPreorder(preorder)
tree = Bintree.BinTree()
tree.horizontallyshow(root, root)