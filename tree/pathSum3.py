# 给定一个二叉树，它的每个结点都存放着一个整数值。

# 找出路径和等于给定数值的路径总数

import Bintree

class Solution(object):
    # res = []
    # def pathSum(self, root, sum):
    #     """
    #     :type root: TreeNode
    #     :type sum: int
    #     :rtype: int
    #     """
    #     if root == None:
    #         return 0
    #     self.res = []
    #     path = []
    #     q = []
    #     q.append(root)
    #     while(q):
    #         size = len(q)
    #         for i in range(0, size):
    #             cur = q.pop(0)
    #             self.nodepathSum(cur, sum, path)
    #             if cur.left:
    #                 q.append(cur.left)

    #             if cur.right:
    #                 q.append(cur.right)
                
    #     #return len(self.res)
    #     return self.res

    # def nodepathSum(self, root, sum, path):
    #     if root == None:
    #         return
        
    #     if sum - root.val == 0:
    #         self.res.append(path + [root.val])
        
        
    #     self.nodepathSum(root.left, sum-root.val, path + [root.val])
    #     self.nodepathSum(root.right, sum - root.val, path + [root.val])

    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefixSumCount = {}
        prefixSumCount[0] = 1
        return self.recursionPathSum(root, prefixSumCount, sum, 0)
    
    def recursionPathSum(self, root, prefixSumCount, sum, currSum):
        if root == None:
            return 0

        res = 0

        currSum += root.val

        res += prefixSumCount.get(currSum-sum, 0)

        prefixSumCount[currSum] = prefixSumCount.get(currSum, 0) + 1

        res += self.recursionPathSum(root.left, prefixSumCount, sum, currSum)
        res += self.recursionPathSum(root.right, prefixSumCount, sum, currSum)

        prefixSumCount[currSum] = prefixSumCount[currSum] - 1

        return res
        


root = [1,-2,-3,1,3,-2,None,-1]

sum = -1
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.pathSum(tree.root, sum))