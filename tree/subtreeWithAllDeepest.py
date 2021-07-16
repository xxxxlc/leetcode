# 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。

# 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。

# 一个节点的 子树 是该节点加上它的所有后代的集合。

# 返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点

import Bintree

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.depthest = []
        self.maxdepth = 0
        self.dfs(root, 0)

        # for node in self.depthest:
        #     print(node.val)
        while(len(self.depthest) > 1):
            self.helper(root, self.depthest.pop(0), self.depthest.pop(0))
            for node in self.depthest:
                print(node.val)
        return self.depthest[0]

    def helper(self, root, p, q):
        if root == None:
            return False
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)

        if (left and right) or (((root.val == p.val) or (root.val == q.val)) and (left or right)):
            self.depthest.append(root)
        
        return left or right or (root.val == p.val) or (root.val == q.val)
    
    def dfs(self, root, depth):
        if root == None:
            return
        depth = depth + 1
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)

        if root.left == None and root.right == None:
            if depth > self.maxdepth:
                self.maxdepth = depth
                self.depthest = []
                self.depthest.append(root)
            elif depth == self.maxdepth:
                self.depthest.append(root)



root = [1,1,None,3,2,6,None,5,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
root = a.subtreeWithAllDeepest(tree.root)
tree.horizontallyshow(root, root)