# 根据一棵树的前序遍历与中序遍历构造二叉树.

import Bintree

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] or inorder == []:
            return None
        root = Bintree.TreeNode(preorder[0])

        left_tree_inorder = inorder[0:inorder.index(preorder[0])]
        right_tree_inorder = inorder[inorder.index(preorder[0])+1:len(inorder)]

        left_tree_preorder = preorder[1:1 + len(left_tree_inorder)]
        right_tree_preorder = preorder[1 + len(left_tree_inorder):len(preorder)]

        left_root = self.buildTree(left_tree_preorder, left_tree_inorder)
        right_root = self.buildTree(right_tree_preorder, right_tree_inorder)
        
        root.left = left_root
        root.right = right_root

        return root






root = [3,9,20,None,None,15,17]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.preOrderTraversal(tree.root)
tree.inOrderTraversal(tree.root)
# print(tree.preorder)
# print(tree.inorder)

a = Solution()
root = a.buildTree(tree.preorder, tree.inorder)
tree.horizontallyshow(root, root)
