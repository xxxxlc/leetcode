# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

import os
import sys
sys.path.append('D:\programming\leetcode\\tree')
import Bintree

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        res = self.helper(root)
        return max(res[0], res[1])

    def helper(self, root):
        if root == None:
            return [0,0]
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        rob = root.val + left[1] + right[1]
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return [rob, not_rob]

root = [3,2,3,None,3,None,1]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.rob(tree.root))