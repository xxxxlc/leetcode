# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
import Bintree
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        def f(root):
            if root == None:
                return 
            f(root.left)
            result.append(root.val)
            f(root.right)
        
        f(root)

        return result


a = [1,None,2,3]
tree = Bintree.BinTree()
tree.CreateTree(a)

tree.preOrderTraversal(tree.root)

b = Solution()
print(b.inorderTraversal(tree.root))



