# 给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

# 二叉树的根是数组 nums 中的最大元素。
# 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
# 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
# 返回有给定数组 nums 构建的 最大二叉树 。

import Bintree

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root_index = nums.index(max(nums))
        root = Bintree.TreeNode(nums[root_index])
        root.left = self.constructMaximumBinaryTree(nums[:root_index])
        root.right = self.constructMaximumBinaryTree(nums[root_index+1:])

        return root


nums = [3,2,1,6,0,5]
a = Solution()
tree = Bintree.BinTree()
root = a.constructMaximumBinaryTree(nums)
tree.horizontallyshow(root, root)