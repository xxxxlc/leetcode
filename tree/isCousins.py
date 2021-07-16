# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

# 如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

# 我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

import Bintree
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        result = False
        q = []
        father_x = None
        father_y = None
        q.append(root)
        while(q):
            size = len(q)
            for i in range(0, size):
                cur = q.pop(0)
                

                if cur.left:
                    q.append(cur.left)
                    if cur.left.val == x:
                        father_x = cur
                    if cur.left.val == y:
                        father_y = cur
                if cur.right:
                    q.append(cur.right)
                    if cur.right.val == x:
                        father_x = cur
                    if cur.right.val == y:
                        father_y = cur

            if father_x != None and father_y != None and father_x != father_y:
                result = True
                break
            else:
                if father_x != None or father_y != None:
                    break

        return result



root1 = [1,2,3,4,5]
tree1 = Bintree.BinTree()
tree1.CreateTree(root1)

a = Solution()
x = 5
y = 4
print(a.isCousins(tree1.root, x, y))
