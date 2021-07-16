# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

import Bintree
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def f(root):
            if root == None:
                return 0
            
            L = f(root.left)
            R = f(root.right)
            self.ans = max(self.ans, L + R + 1)
            
            return max(L, R) + 1

        f(root)

        return self.ans - 1

root = [1,2,3,4,5]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.diameterOfBinaryTree(tree.root))
