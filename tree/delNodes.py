# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。

# 如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

# 返回森林中的每棵树。你可以按任意顺序组织答案。

import Bintree

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        self.res = []
        if root.val not in to_delete:
            self.res.append(root)
        self.helper(root, to_delete)


        return self.res

    def helper(self, root, to_delete):
        if root == None:
            return
        
        root.left = self.helper(root.left, to_delete)
        root.right = self.helper(root.right, to_delete)

        if root.val in to_delete:
            if root.left:
                self.res.append(root.left)
            if root.right:
                self.res.append(root.right)
            root = None
            return root
        
        return root
        


root = [1,2,3,None,None,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

to_delete = [2, 1]
a = Solution()
froest = a.delNodes(tree.root, to_delete)

for t in froest:
    tree.horizontallyshow(t, t)