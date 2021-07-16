# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。

import Bintree

class Solution(object):
    def sumRootToLeaf(self, root):
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
            res += pow(2, size - i - 1) * n[i]
        return res


        

root = [0]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.sumRootToLeaf(tree.root))