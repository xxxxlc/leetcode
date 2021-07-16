# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：

# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。


import Bintree

class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        
        q = []
        q.append(root)
        depth = 0
        while(q):
            size = len(q)
            temp = 0
            for i in range(0, size):
                cur = q.pop(0)
                if depth % 2 == 0:
                    if cur.val % 2 == 0:
                        return False
                    if temp == 0:
                        temp = cur.val
                    else:
                        if cur.val <= temp:
                            return False
                        temp = cur.val
                else:
                    if cur.val % 2 != 0:
                        return False
                    if temp == 0:
                        temp = cur.val
                    else:
                        if cur.val >= temp:
                            return False
                        temp = cur.val

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            depth += 1
        
        return True

root = [5,4,2,3,3,7]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.isEvenOddTree(tree.root))