# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

import Bintree

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        res = []
        res = self.findminmax(root, res)
        if len(res) < 2:
            return False
        l = 0
        r = len(res) - 1
        while(l < r):
            if res[l] + res[r] == k:
                return True
            
            if res[l] + res[r] < k:
                l = l + 1
            elif res[l] + res[r] > k:
                r = r - 1
        
        return False

    
    def findminmax(self, root, res):
        if root == None:
            return res
        
        res = self.findminmax(root.left, res)
        res.append(root.val)
        res = self.findminmax(root.right,res)

        return res


root = [2,1,3]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

k = 28
a = Solution()
print(a.findTarget(tree.root, k))