class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.left_pass_on = True
        self.right_pass_on = True
        self.next = None

class BinTree(object):
    def __init__(self, root=None):
        self.root = root
        self.ls = []
        self.preorder = []
        self.inorder = []
        self.postorder = []
    
    def CreateTree(self, nodes):
        for node in nodes:
            if self.root == None:
                if node:
                    self.root = TreeNode(node)
                    self.ls.append(self.root)
                    continue
                else:
                    return 0
            rootnode = self.ls[0]
            if node == None:
                if rootnode.left_pass_on == True and rootnode.left == None:
                    rootnode.left_pass_on = False
                    continue
                if rootnode.right_pass_on == True and rootnode.right == None:
                    rootnode.right_pass_on = False
                    self.ls.pop(0)
                    continue
            else:
                treenode = TreeNode(node)
                if rootnode.left == None and rootnode.left_pass_on == True:
                    rootnode.left = treenode
                    self.ls.append(treenode)
                elif rootnode.right == None and rootnode.right_pass_on == True:
                    rootnode.right = treenode
                    self.ls.append(treenode)
                    self.ls.pop(0)
                else:
                    return 0
    
    def preOrderTraversal(self, root):
        if root == None:
            return
        # print(root.val)
        self.preorder.append(root.val)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root):
        if root == None:
            return
        # print(root.val)
        self.inOrderTraversal(root.left)
        self.inorder.append(root.val)
        self.inOrderTraversal(root.right)
    
    def postOrderTraversal(self, root):
        if root == None:
            return
        # print(root.val)
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        self.postorder.append(root.val)

    def heightOfBT(self, root):
        if root == None:
            return 0
        HL = self.heightOfBT(root.left)
        HR = self.heightOfBT(root.right)

        if HL > HR:
            return HL + 1
        else:
            return HR + 1



    def __str__(self):
        result = ''
        self.height = self.heightOfBT(self.root)
        self.width = 2^(self.height-1)*4
        depth = 1
        q = []
        space = (2**(self.height-1) - 1)*" "
        result = result + space + str(self.root.val).format(2) + '\n'
        q.append(self.root)
        while(depth < self.height):
            size = len(q)
            space = (2**(self.height - 1 - depth) - 1)*' '
            for i in range(0, size):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                    result = result + space + str(cur.left.val).format(2) + space
                result = result + " "
                if cur.right:
                    q.append(cur.right)
                    result = result + space + str(cur.right.val).format(2) + space
                result = result + " "


            result = result + '\n'
            depth = depth + 1

        return result

    def findroot(self, val):
        q = []
        q.append(self.root)
        while(q):
            size = len(q)
            for i in range(0, size):
                node = q.pop(0)
                if node.val == val:
                    return node
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

    def horizontallyshow(self, parent, root, prefix=''):
        prefix = prefix + '|'
        if root:
            print(prefix + '--' + str(root.val))
            if (root == parent or root == parent.right):
                prefix = prefix[0:len(prefix)-1]
                prefix = prefix + ' '
            self.horizontallyshow(root, root.left, prefix+'  ')
            self.horizontallyshow(root, root.right, prefix+'  ')
        else:
            if(parent.right or parent.right):
                print(prefix + '--' + '{ }')
            

    def verticallyshow(self, root):
        q = []
        q.append(root)
        InOrd = ''
        self.InOrderTraversal(root, InOrd)
        while(q):
            cache = []
            while(q):
                node = q.pop(0)
                cache.append(node)
            line = []
            for node in cache:
                if node:
                    line[InOrd.find(str(node.val))] = node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            print(line)



    def InOrderTraversal(self, root, In):
        if root:
            self.InOrderTraversal(root.left, In)
            In = In + str(root.val)
            self.InOrderTraversal(root.right, In)



# 二叉搜索树
class BST(BinTree):
    def __init__(self):
        super().__init__()

    def isValidBST(self, root):
        return self.isValidBST_m(root, None, None)
    
    def isValidBST_m(self, root, min, max):
        if root == None:
            return True
        
        if min and root.val <= min.val:
            return False
        
        if max and root.val >= max.val:
            return False
        
        return self.isValidBST_m(root.left, min, root) and self.isValidBST_m(root.right, root, max)

    def isInBST(self, root, target):
        if root == None:
            return False
        if root.val < target:
            return self.isInBST(root.right, target)
        
        elif root.val > target:
            return self.isInBST(root.left, target)

        elif root.val == target:
            return True
    
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        return root
    
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






















if __name__ == "__main__":
    # a = [3,9,2,None,None,1,7]
    # tree = BinTree()
    # tree.CreateTree(a)
    # print(tree)
    # tree.preOrderTraversal(tree.root)
    # print(tree.heightOfBT(tree.root))
    # print(tree.findroot(3))
    # tree.horizontallyshow(tree.root, tree.root)
    # tree.verticallyshow(tree.root)

    b = [2,1,3]
    tree1 = BST()
    tree1.CreateTree(b)
    tree1.horizontallyshow(tree1.root, tree1.root)
    print(tree1.isValidBST(tree1.root))
            

            

