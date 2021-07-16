# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）

import Bintree

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def f(root, res):
            if root == None:
                return res

            res = f(root.left, res)
            
            res.append(root.val)
            res = f(root.right, res)

            return res
        res = f(root, res)
        return res[k - 1]

root = [3, 1, 4, None, 2]
tree = Bintree.BinTree()
tree.CreateTree(root)

k = 1
a = Solution()
print(a.kthSmallest(tree.root, k))
