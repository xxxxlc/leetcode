# 给定两个二叉树，编写一个函数来检验它们是否相同。

# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
    def preOrderTraversal(self,root):
        if root == None:
            return
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traverse(p, q):
            if p == None and q == None:
                return True
            
            if p == None or q == None:
                return False
            
            if p.val != q.val:
                return False

            traverse(p.left, q.left)
            if traverse(p.left, q.left) == False:
                return False
            result = traverse(p.right, q.right)
            return result

        return traverse(p, q)

a = [1,2,1]
b = [1,1,2]
tree_a = BinTree()
tree_b = BinTree()
for i in a:
    tree_a.add(i)

for i in b:
    tree_b.add(i)
# tree.preOrderTraversal(tree.root)

c = Solution()
print(c.isSameTree(tree_a.root, tree_b.root))

