# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

# 假定 BST 有如下定义：

# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
import Bintree

class Solution(object):
    def __init__(self):
        self.base = None
        self.maxcount = 0
        self.count = 0
        self.result = []

    def update(self, x):
        if x == self.base:
            self.count = self.count + 1
        else:
            self.base = x
            self.count = 1
        if self.count == self.maxcount:
            self.result.append(x)
        if self.count > self.maxcount:
            self.maxcount = self.count
            self.result = []
            self.result.append(x)
        

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root == None:
        #     return
        # self.findMode(root.left)
        # self.update(root.val)
        # print(self.result)
        # self.findMode(root.right)

        # return self.result

        cur = root
        pre = None
        while(cur):
            if cur.left == None:
                self.update(cur.val)
                cur = cur.right
                continue
            pre = cur.left
            while(pre.right != None and pre.right != cur):
                pre = pre.right
            if pre.right == None:
                pre.right = cur
                cur = cur.left
            elif pre.right == cur:
                self.update(cur.val)
                cur = cur.right
            
        return self.result



root = [1,None,2,2]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.findMode(tree.root))

