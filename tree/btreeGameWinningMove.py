# 「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。

# 「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。

 

# 之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。

# 如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。

# 若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

 

# 现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。

import Bintree

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        if root == None:
            return False
        self.ans = False
        self.helper(root, x, n)

        return self.ans
    
    def helper(self, root, x, n):
        if root == None:
            return 0
        
        left = self.helper(root.left, x, n)
        right = self.helper(root.right, x, n)

        if root.val == x:
            self.ans = max(left, right, n - left - right - 1) > n/2
            
        return left + right + 1
        



root = [1,2,3,4,5,6,7,8,9,10,11]
tree = Bintree.BinTree()
tree.CreateTree(root)

n = 11
x = 3

a = Solution()
print(a.btreeGameWinningMove(tree.root, n, x))