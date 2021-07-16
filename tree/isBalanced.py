# 给定一个二叉树，判断它是否是高度平衡的二叉树。

import Bintree
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root):
            if root == None:
                return 1
            HL = f(root.left)
            HR = f(root.right)
            if HL != False and HR != False:
                if abs(HL - HR) > 1:
                    return False
                else:
                    if HL > HR:
                        return HL + 1
                    else:
                        return HR + 1
            else:
                return False
        
        result = f(root)
        if result == False:
            return False
        else:
            return True
        

root = [1,2,2,3,3,None,None,4,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
# tree.preOrderTraversal(tree.root)

a = Solution()
print(a.isBalanced(tree.root))