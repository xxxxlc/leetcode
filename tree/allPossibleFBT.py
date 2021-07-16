# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

# 答案中每个树的每个结点都必须有 node.val=0。

# 你可以按任何顺序返回树的最终列表。

import Bintree
from Bintree import TreeNode

class Solution(object):
    res = {0:[], 1: [TreeNode(0)]}
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n not in self.res:
            ans = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            self.res[n] = ans
        
        return self.res[n]

n = 7
a = Solution()
root = a.allPossibleFBT(n)