# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

# 请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

import Bintree

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None
        
        q = []
        q.append(root)
        maxdepth = 0
        depth = 0
        maxval = float('-inf')
        while(q):
            depthsum = 0
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)
                print(cur.val)
                depthsum += cur.val
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
            print('\n')
            # print(depthsum)
            depth += 1
            if depthsum > maxval:
                maxval = depthsum
                maxdepth = depth
        
        return maxdepth


root = [989,None,10250,98693,-89388,None,None,None,-32127]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.maxLevelSum(tree.root))