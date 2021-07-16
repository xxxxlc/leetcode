# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL

import Bintree

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        q = []
        q.append(root)
        res = []
        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                
                res.append(cur.val)
                if i < size - 1:
                    cur.next = q[0]
                else:
                    res.append('#')
        
        return root
        


root = [1,2,3,4,5,6,7]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.connect(tree.root))