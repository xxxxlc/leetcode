# 给定一个二叉树，检查它是否是镜像对称的。

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinTree():
    def __init__(self):
        self.root = None
        self.ls = []
    
    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(node)
        else:
            rootnode = self.ls[0]
            if rootnode.left == None:
                rootnode.left = node
                self.ls.append(node)
            elif rootnode.right == None:
                rootnode.right = node
                self.ls.append(node)
                self.ls.pop(0)
    
    def preOrderTraversal(self, root):
        if root == None:
            return
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(p, q):
            if (not p and not q):
                return True
            if (not p or not q):
                return False
            if p.val == q.val and check(p.left, q.right) and check(p.right, q.left):
                return True
            else:
                return False
        return check(root, root)



t = [1,2,2,None,3,3]
tree = BinTree()
for node in t:
    tree.add(node)
# tree.preOrderTraversal(tree.root)

a = Solution()
print(a.isSymmetric(tree.root))