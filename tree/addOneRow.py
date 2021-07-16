# 给定一个二叉树，根节点为第1层，深度为 1。在其第 d 层追加一行值为 v 的节点。

# 添加规则：给定一个深度值 d （正整数），针对深度为 d-1 层的每一非空节点 N，为 N 创建两个值为 v 的左子树和右子树。

# 将 N 原先的左子树，连接为新节点 v 的左子树；将 N 原先的右子树，连接为新节点 v 的右子树。

# 如果 d 的值为 1，深度 d - 1 不存在，则创建一个新的根节点 v，原先的整棵树将作为 v 的左子树。

import Bintree

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if root == None:
            root = Bintree.TreeNode(val)
            return root
        if depth == 1:
            root1 = Bintree.TreeNode(val)
            root1.left = root
            return root1
        q = []
        q.append(root)
        d = 1

        while(q):
            if d == depth-1:
                break
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            d = d + 1

        for node in q:
            left = Bintree.TreeNode(val)
            right = Bintree.TreeNode(val)
            left.left = node.left
            right.right = node.right
            node.left = left
            node.right = right
        
        return root

root = [4,2,6,3,1,5]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
val = 1
depth = 2
root = a.addOneRow(tree.root, val, depth)
tree.horizontallyshow(root, root)