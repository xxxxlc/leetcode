# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

import Bintree
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
            else:
                return
        
        dfs(root)

        q = [(target, 0)]
        seen = {target}

        while(q):
            if q[0][1] == K:
                return [node.val for node, d in q]
            
            node, d = q.pop(0)

            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    q.append((nei, d + 1))
        
        return []


    


root = [3,5,1,6,2,0,8,None,None,7,4]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

target = 5
K = 2

a = Solution()
print(a.distanceK(tree.root, target, K))
