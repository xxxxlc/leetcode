# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
import Bintree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        result = root
        while(True):
            if p.val < result.val and q.val < result.val:
                result = result.left
            elif p.val > result.val and q.val > result.val:
                result = result.right
            else:
                break
        return result


root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 4
tree = Bintree.BinTree()
tree.CreateTree(root)
p = tree.findroot(p)
q = tree.findroot(q)
# tree.preOrderTraversal(tree.root)

a = Solution()
answer = a.lowestCommonAncestor(tree.root, p, q)
print(answer.val)