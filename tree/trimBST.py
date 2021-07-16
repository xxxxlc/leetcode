# 给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。
# 修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

# 所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。


import Bintree

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root == None:
            return None


        if root.val < low:
            
            root = root.right
            root = self.trimBST(root, low, high)
            
        
        elif root.val > high:
            root = root.left
            root = self.trimBST(root, low, high)
            

        else:
            root.left = self.trimBST(root.left,low,high)
            root.right = self.trimBST(root.right,low,high)
        
        return root
        

        

    

root = [3,1,4,None,2]
tree = Bintree.BinTree()
tree.CreateTree(root)


a = Solution()
low = 1
high = 2
root = a.trimBST(tree.root, low, high)
tree.horizontallyshow(root, root)