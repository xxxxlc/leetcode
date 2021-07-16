# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

import Bintree

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        return self.isSame(s ,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    
    def isSame(self, x, y):
        if x == None and y == None:
            return True
        elif x == None or y == None:
            return False
        if x.val != y.val:
            return False
        
        return self.isSame(x.left, y.left) and self.isSame(x.right, y.right)

s = [3,4,5,1,2,None,None,None,None,0]
t = [4,1,2]
tree_s = Bintree.BinTree()
tree_s.CreateTree(s)
tree_t = Bintree.BinTree()
tree_t.CreateTree(t)
tree_s.horizontallyshow(tree_s.root, tree_s.root)

a = Solution()
# print(a.isSame(tree_s.root, tree_t.root))
print(a.isSubtree(tree_s.root, tree_t.root))


