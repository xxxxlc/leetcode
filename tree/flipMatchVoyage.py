# 给你一棵二叉树的根节点 root ，树中有 n 个节点，每个节点都有一个不同于其他节点且处于 1 到 n 之间的值。

# 另给你一个由 n 个值组成的行程序列 voyage ，表示 预期 的二叉树 先序遍历 结果。

# 通过交换节点的左右子树，可以 翻转 该二叉树中的任意节点。例，翻转节点 1 的效果如下：

import Bintree

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        if root == None:
            if len(voyage) == 0:
                return []
            else:
                return -1
        self.res = []
        if self.helper(root, voyage):
            return self.res
        
        return -1
    
    def helper(self, root, voyage):
        if root == None:
            if len(voyage) == 0:
                return True
            else:
                return False
        if  len(voyage) == 0 or voyage[0] != root.val:
            return False
        
        if root.left == None:
            return self.helper(root.right, voyage[1:])
        if root.right == None:
            return self.helper(root.left, voyage[1:])
        if len(voyage) < 2:
            return False
        if root.left.val != voyage[1]:
            if root.left.val not in voyage:
                return False
            left = voyage.index(root.left.val)
            self.res.append(root.val)
            return self.helper(root.left, voyage[left:]) and self.helper(root.right, voyage[1:left])
        else:
            if root.right.val not in voyage:
                return False
            right = voyage.index(root.right.val)
            return self.helper(root.left,voyage[1:right]) and self.helper(root.right, voyage[right:])



            


root = [1,2,3]
voyage = [1,2,3]

tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.flipMatchVoyage(tree.root, voyage))