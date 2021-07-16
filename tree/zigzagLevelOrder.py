# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
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
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0]
            if rootNode.left == None:
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None:
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0)

    def preOrderTraversal(self,root):
        if root == None:
            return 
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        cur = []
        cur.append(root)
        switch = False
        while (cur):
            level = []
            cur_next = []
            print(cur)
            for node in cur:
                if node.val != None:
                    level.append(node.val)
                if node.left != None:
                    cur_next.append(node.left)
                if node.right != None:
                    cur_next.append(node.right)
            cur = cur_next
            if switch == False:
                switch = True
                result.append(level)
            else:
                switch = False
                result.append(level[::-1])
        return result

        

l = [0,2,4,1,None,3,-1,5,1,None,6,None,8]
tree = BinTree()
for element in l:
    tree.add(element)

tree.preOrderTraversal(tree.root)

a = Solution()
print(a.zigzagLevelOrder(tree.root))




