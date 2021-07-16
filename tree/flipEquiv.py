# 我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。

# 只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。

# 编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。

import Bintree

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is root2:
            return True
        
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) or 
                self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

root1 = [1,2,3,4,5,6,None,None,None,7,8]
root2 = [1,3,2,None,6,4,5,None,None,None,8,7]

tree1 = Bintree.BinTree()
tree2 = Bintree.BinTree()

tree1.CreateTree(root1)
tree2.CreateTree(root2)

a = Solution()
print(a.flipEquiv(tree1.root, tree2.root))