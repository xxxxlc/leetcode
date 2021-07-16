# 给你一个树，请你 按中序遍历 重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

import Bintree

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        res = self.inordertraversal(root, res)
        root = Bintree.TreeNode(res.pop(0))
        node = root
        while(res):
            node_val = res.pop(0)
            if node == None:
                root.val = node_val
                continue
            
            cur = Bintree.TreeNode()
            cur.val = node_val
            node.right = cur
            node = cur

        return root
    
    def inordertraversal(self, root, res):
        if root == None:
            return []

        self.inordertraversal(root.left, res)
        res.append(root.val)
        self.inordertraversal(root.right, res)

        return res


root = [5,3,6,2,4,None,8,1,None,None,None,7,9]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
tree.horizontallyshow(a.increasingBST(tree.root), a.increasingBST(tree.root))
