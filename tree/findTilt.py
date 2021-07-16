# 给定一个二叉树，计算 整个树 的坡度 。

# 一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

# 整个树 的坡度就是其所有节点的坡度之和。
import Bintree

class Solution(object):
    tilt = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sumnode(root)

        return self.tilt
    
    def sumnode(self, root):
        if root == None:
            return 0
        
        left = self.sumnode(root.left)
        right = self.sumnode(root.right)
        # print(root.val, left, right)
        self.tilt = self.tilt + abs(left - right)

        return root.val + left + right



root = [4,2,9,3,5,None,7]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.findTilt(tree.root))