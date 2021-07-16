# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

# 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树


import Bintree

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        
        return ' '.join(map(str, postorder(root)))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = Bintree.TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)

            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return helper()

root = [2,1,3]
tree = Bintree.BinTree()
tree.CreateTree(root)

ser = Codec()
deser = Codec()
tree_1 = ser.serialize(tree.root)
print(tree_1)
ans = deser.deserialize(tree_1)
tree.horizontallyshow(ans, ans)