# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

import Bintree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, left, right):
            if left>right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums, left, mid - 1)
            root.right = helper(nums, mid+1, right)
            return root
        
        return helper(nums, 0, len(nums) - 1)






a = Solution()
nums = [-10,-3,0,5,9]
root = a.sortedArrayToBST(nums)
tree = Bintree.BinTree()
tree.preOrderTraversal(root)
