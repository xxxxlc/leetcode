# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

import Bintree
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return None
        
        q = [(root, 0, 0)]
        cur_depth = left = ans = 0

        for node, depth, pos in q:
            if node:
                q.append((node.left, depth+1, 2*pos))
                q.append((node.right, depth+1, 2*pos+1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                
                ans = max(pos - left + 1, ans)
        
        return ans
            

root = [1,3,2,5,3,None,9]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.widthOfBinaryTree(tree.root))