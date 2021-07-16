# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

# 更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

import Bintree
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        min = float('inf')
        sec_min = float('inf')

        min, sec_min = self.findsecondmin(root, min, sec_min)
        if sec_min == float('inf'):
            return -1
        return sec_min
    
    def findsecondmin(self, root, min, sec_min):
        if root == None:
            return min, sec_min
        
        if root.val < min:
            sec_min = min
            min = root.val
        elif root.val > min and root.val < sec_min:
            sec_min = root.val
        min, sec_min = self.findsecondmin(root.left, min, sec_min)
        min, sec_min = self.findsecondmin(root.right, min, sec_min)

        return min, sec_min


node = [2,2,2]
tree = Bintree.BinTree()
tree.CreateTree(node)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.findSecondMinimumValue(tree.root))