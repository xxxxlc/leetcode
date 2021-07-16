# 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。

# 找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。

# （小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）

import Bintree

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.paths = "~"
        path = []
        self.helper(root, path)
        return self.paths
    
    def helper(self, root, path):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            p = "".join(reversed(path[:] + [chr(ord('a') + root.val)]))
            self.paths = min(self.paths, p)
        
        path.append(chr(ord('a') + root.val))
        self.helper(root.left, path)
        self.helper(root.right, path)
        path.pop(-1)


root = [1,1,2,3,4,3,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)
a = Solution()
print(a.smallestFromLeaf(tree.root))