#给定一个二叉树，找出其最小深度。

#最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

#说明：叶子节点是指没有子节点的节点。

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Bintree():
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
    
    def removeNone(self, root):
        if root.left == None:
            pass
        else:
            if root.left.val == None:
                root.left = None
            else:
                self.removeNone(root.left)

        if root.right == None:
            pass
        else:
            if root.right.val == None:
                root.right = None
            else:
                self.removeNone(root.right)

    

    
    def preOrderTraversal(self, root):
        if root == None:
            return
        print(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = []
        depth = 1
        q.append(root)

        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)

                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            
            depth = depth + 1
        
        return depth

root = [2,None,3,None,4,None,5,None,6]
bintree = Bintree()
for node in root:
    bintree.add(node)
# bintree.removeNone(bintree.root)
bintree.preOrderTraversal(bintree.root)

a = Solution()
print(a.minDepth(bintree.root))
