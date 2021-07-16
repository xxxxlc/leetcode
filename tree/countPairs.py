# 给你二叉树的根节点 root 和一个整数 distance 。

# 如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

# 返回树中 好叶子节点对的数量 。

import Bintree

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        if root == None:
            return 0
        _,res = self.helper(root, distance)
        return res
    
    def helper(self, root, distance):
        depths = [0] * (distance + 1)

        if root.left == None and root.right == None:
            depths[0] = 1
            return (depths, 0)

        leftDepths = [0] * (distance + 1)
        rightDepths = [0] * (distance + 1)
        leftCount = rightCount = 0

        if root.left:
            leftDepths, leftCount = self.helper(root.left, distance)

        if root.right:
            rightDepths, rightCount = self.helper(root.right, distance)
        
        for i in range(0, distance):
            depths[i + 1] += leftDepths[i]
            depths[i + 1] += rightDepths[i]

        cnt = 0
        for i in range(0, distance + 1):
            for j in range(distance - i - 1):
                cnt += leftDepths[i] * rightDepths[j]
        return (depths, cnt + leftCount + rightCount)

        



root = [1,2,3,4,5,6,7]
tree = Bintree.BinTree()
tree.CreateTree(root)

distance = 3
a = Solution()
print(a.countPairs(tree.root, distance))