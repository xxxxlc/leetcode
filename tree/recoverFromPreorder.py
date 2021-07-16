# 我们从二叉树的根节点 root 开始进行深度优先搜索。

# 在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

# 如果节点只有一个子节点，那么保证该子节点为左子节点。

# 给出遍历输出 S，还原树并返回其根节点 root。

import Bintree

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: TreeNode
        """
        if traversal == '':
            return None

        traversal = list(traversal)
        stringnum = []
        s = ''
        for char in traversal:
            if char == '-':
                if s != '':
                    stringnum.append(int(s))
                    s = ''
                stringnum.append(char)
            else:
                s = s + char
        stringnum.append(int(s))
        print(stringnum)
        return self.helper(stringnum, 0)
    
    def helper(self, traversal, depth0):
        if traversal == None:
            return None
        
        root = Bintree.TreeNode(int(traversal[0]))
        depth = 0
        index = []
        for i in range(0, len(traversal)):
            if traversal[i] == '-':
                depth += 1
            else:
                if depth == depth0 + 1:
                    index.append(i)
                    if len(index) == 2:
                        break
                depth = 0
        if len(index) == 0:
            return root
        if len(index) == 1:
            root.left = self.helper(traversal[index[0]:], depth0 + 1)
            return root
        root.left = self.helper(traversal[index[0]:index[1]-depth0-1], depth0 + 1)
        root.right = self.helper(traversal[index[1]:], depth0+1)
        

        return root


traversal = "1-401--349---90--88"
tree = Bintree.BinTree()
a = Solution()
root = a.recoverFromPreorder(traversal)
tree.horizontallyshow(root, root)