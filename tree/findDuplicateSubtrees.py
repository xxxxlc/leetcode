# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

# 两棵树重复是指它们具有相同的结构以及相同的结点值。

import Bintree

class Solution(object):
    dict_tree = {}
    res = []
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.dict_tree = {}
        self.res = []
        self.traverse(root)

        return self.res

    

    def traverse(self, root):
        if root == None:
            return '#'
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        subTree = left + ',' + right + ',' + str(root.val)

        self.dict_tree[subTree] = self.dict_tree.get(subTree, 0) + 1
        if self.dict_tree[subTree] == 2:
            self.res.append(root)

        return subTree

root = [1,2,3,4,None,2,4,None,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
# tree.horizontallyshow(tree.root, tree.root)

a = Solution()
roots = a.findDuplicateSubtrees(tree.root)
for root in roots:
    tree.horizontallyshow(root, root)
    print('\n')
