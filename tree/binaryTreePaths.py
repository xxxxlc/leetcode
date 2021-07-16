# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
import Bintree

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        path = []
        output = []
        def find(root,path):
            if root == None:
                return
            if root.right == None and root.left == None:
                result.append(path + [root.val])
                return
            find(root.left, path + [root.val])
            find(root.right, path + [root.val])
        find(root, path)
        for i in result:
            s = str(i[0])
            for j in range(1, len(i)):
                s = s + '->' + str(i[j])
            output.append(s)
        return output

a = [1,2,3,None,5]
tree = Bintree.BinTree()
tree.CreateTree(a)
# tree.preOrderTraversal(tree.root)

b = Solution()
print(b.binaryTreePaths(tree.root))
