# 给出一个满足下述规则的二叉树：

# root.val == 0
# 如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 1
# 如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x + 2
# 现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。

# 请你先还原二叉树，然后实现 FindElements 类：

# FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。
# bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。



import Bintree
from Bintree import TreeNode

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.dict = {}
        self.root = root
        if root == None:
            pass
        else:
            def helper(root, val):
                if root == None:
                    return
                root.val = val
                self.dict[root.val] = 1
                helper(root.left, 2 * root.val + 1)
                helper(root.right, 2 * root.val + 2)
            
            helper(root, 0)


    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        if target in self.dict:
            return True
        
        return False



root = [-1, None, -1]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = FindElements(tree.root)
tree.horizontallyshow(tree.root, tree.root)