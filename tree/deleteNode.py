# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：

# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度

import Bintree

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            
            if not (root.left or root.right):
                root = None
            
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
            

    
    def successor(self, root):
        root = root.right
        while(root.left):
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while(root.right):
            root = root.right
        return root.val



root = [5,3,6,2,4,None,7]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
key = 7
root = a.deleteNode(tree.root, key)
tree.horizontallyshow(root, root)