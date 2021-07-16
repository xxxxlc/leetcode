# 给定一个 N 叉树，返回其节点值的层序遍历

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root == None:
            return None

        q = []
        q.append(root)
        res = []
        depth = 0
        while(q):
            size = len(q)
            res.append([])
            for i in range(0, size):
                cur = q.pop(0)
                res[depth].append(cur.val)
                
                for child in cur.children:
                    if child:
                        q.append(child)
            depth += 1
        
        return res