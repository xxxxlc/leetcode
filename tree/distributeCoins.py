# 给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。

# 在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

# 返回使每个结点上只有一枚硬币所需的移动次数。

import Bintree

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root == None:
            return 0
        
        L = self.dfs(root.left)
        R = self.dfs(root.right)

        self.res += abs(L) +abs(R)
        return root.val + L + R - 1


root = [3,0,0]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.distributeCoins(tree.root))
