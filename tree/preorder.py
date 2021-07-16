# 给定一个 N 叉树，返回其节点值的 前序遍历 。

# N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

class Solution(object):
    res = []
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.preorder_find(root)
        return self.res
    
    def preorder_find(self, root):
        if root == None:
            return
        self.res.append(root.val)

        for child in root.children:
            self.preorder_find(child)

