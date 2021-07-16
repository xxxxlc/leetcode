# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

import Bintree
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        def f(root, sum, path):
            if root == None:
                return
            if root.left == None and root.right == None and sum == root.val:
                result.append(path + [root.val])
            else:
                # print(path)
                f(root.left, sum - root.val, path + [root.val])
                f(root.right, sum - root.val, path + [root.val])
        
        f(root, targetSum, path)

        return result


a = [5,4,8,11,None,13,4,7,2,None,None,5,1]
tree = Bintree.BinTree()
tree.CreateTree(a)
# tree.preOrderTraversal(tree.root)

b = Solution()
targetSum = 22
print(b.pathSum(tree.root, targetSum))