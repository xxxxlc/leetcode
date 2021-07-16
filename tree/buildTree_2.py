# 根据一棵树的后序遍历与中序遍历构造二叉树.

import Bintree

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            val = postorder.pop()
            root = Bintree.TreeNode(val)

            index = idx_map[val]

            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)

            return root
        
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)






root = [3,9,20,None,None,15,17]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.inOrderTraversal(tree.root)
tree.postOrderTraversal(tree.root)
# print(tree.preorder)
# print(tree.inorder)

a = Solution()
root = a.buildTree(tree.inorder, tree.postorder)
tree.horizontallyshow(root, root)