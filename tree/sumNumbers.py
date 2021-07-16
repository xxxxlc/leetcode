# 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
# 每条从根节点到叶节点的路径都代表一个数字：

# 例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
# 计算从根节点到叶节点生成的 所有数字之和 。

# 叶节点 是指没有子节点的节点。

import Bintree

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        s = []
        def f(root, s, res):
            if root == None:
                return res
            if root.right == None and root.left == None:
                s.append(root.val)
                res += self.sum2(s)
                s.pop(len(s)-1)

            s.append(root.val)
            res = f(root.left, s, res) 
            res = f(root.right, s, res)
            s.pop(len(s)-1)

            return res

        return f(root, s, res)
        
    def sum2(self, n):
        res = 0
        size = len(n)
        for i in range(0, size):
            res += pow(10, size - i - 1) * n[i]
        return res

root = [1,2,3]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.sumNumbers(tree.root))