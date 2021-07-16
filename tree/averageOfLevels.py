# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。


import Bintree
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        q = []
        res = []
        q.append(root)
        while(q):
            size = len(q)
            sum1 = 0
            for i in range(0, size):
                node = q.pop(0)
                sum1 += node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            print(sum1)
            res.append(float(sum1/size))
        
        return res
            


node = [3,9,20,None,None,15,7]
tree = Bintree.BinTree()
tree.CreateTree(node)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.averageOfLevels(tree.root))