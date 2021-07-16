# 给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
import Bintree


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = []
        q = []
        q.append(root)
        while(q):
            n = len(q)
            layer = []
            for i in range(0, n):
                node = q.pop(0)
                layer.append(node.val)
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            result.append(layer)
        result = result[::-1]
        return result




a = [3,9,2,None,None,1,7]
tree = Bintree.BinTree()
tree.CreateTree(a)
tree.preOrderTraversal(tree.root)

b = Solution()
print(b.levelOrderBottom(tree.root))