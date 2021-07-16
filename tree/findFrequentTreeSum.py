# 给你一个二叉树的根结点，请你找出出现次数最多的子树元素和。一个结点的「子树元素和」定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

# 你需要返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

import Bintree

class Solution(object):
    dict_sum = {}
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = []
        self.dict_sum = {}
        self.helper(root)
        max_values = max(self.dict_sum.values())
        for key, value in self.dict_sum.items():
            if value == max_values:
                res.append(key)
        return res
    
    def helper(self, root):
        if root == None:
            return 0
        
        root_sum = root.val + self.helper(root.left) + self.helper(root.right)

        self.dict_sum[root_sum] = self.dict_sum.get(root_sum, 0) + 1
        return root_sum
        
        
        

        

root = [5,2,-5]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.findFrequentTreeSum(tree.root))