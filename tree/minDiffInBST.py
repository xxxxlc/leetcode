# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

import Bintree
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = float('inf')
        res = []
        res = self.min_find(root, res)
        for i in range(0, len(res) - 1):
            if res[i+1] - res[i] < ans:
                ans = res[i+1] - res[i]
        
        return ans
    
    def min_find(self, root, res):
        if root == None:
            return []
        
        self.min_find(root.left, res)
        res.append(root.val)

        self.min_find(root.right, res)

        return res


root = [4,2,6,1,3,None,None]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.minDiffInBST(tree.root))