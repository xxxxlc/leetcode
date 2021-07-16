# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 

import Bintree

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.buildtree(1, n) if n else []

    def buildtree(self, start, end):
        if start > end:
            return [None,]
        
        allTree = []
        for i in range(start, end + 1):
            leftTree = self.buildtree(start, i - 1)
            rightTree = self.buildtree(i + 1, end)
        
            for l in leftTree:
                for r in rightTree:
                    cur = Bintree.TreeNode(i)
                    cur.left = l
                    cur.right = r
                    allTree.append(cur)
        return allTree





n = 3
a = Solution()
tree_list = a.generateTrees(n)
tree = Bintree.BinTree()
for root in tree_list:
    tree.horizontallyshow(root, root)