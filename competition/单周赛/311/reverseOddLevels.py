# 给你一棵 完美 二叉树的根节点 root ，请你反转这棵树中每个 奇数 层的节点值。

# 例如，假设第 3 层的节点值是 [2,1,3,4,7,11,29,18] ，那么反转后它应该变成 [18,29,11,7,4,3,1,2] 。
# 反转后，返回树的根节点。

# 完美 二叉树需满足：二叉树的所有父节点都有两个子节点，且所有叶子节点都在同一层。

# 节点的 层数 等于该节点到根节点之间的边数。

import Bintree from '../../../tree/Bintree'


class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

root = [2,3,5,8,13,21,34]

a = Solution()
print(a.reverseOddLevels)