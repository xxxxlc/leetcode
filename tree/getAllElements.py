# 给你 root1 和 root2 这两棵二叉搜索树。

# 请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.


import Bintree

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        res1 = []
        res2 = []
        res1 = self.helper(root1, res1)
        res2 = self.helper(root2, res2)
        print(res1)
        print(res2)
        res = self.add(res1, res2)
        return res
    
    def helper(self, root, res):
        if root == None:
            return res
        
        res = self.helper(root.left, res)
        res.append(root.val)
        res = self.helper(root.right, res)

        return res
    
    def add(self, res1, res2):
        res = []
        i = 0
        j = 0
        while(len(res) < len(res1) + len(res2) and i < len(res1) and j < len(res2)):
            if res1[i] <= res2[j]:
                res.append(res1[i])
                i += 1
            else:
                res.append(res2[j])
                j += 1

        if len(res) == len(res1) + len(res2):
            return res
        
        else:
            if i != len(res1):
                res.extend(res1[i:len(res1)])
            else:
                res.extend(res2[j:len(res2)])
            
            return res


root1 = [0,-10,10]
root2 = [5,1,7,0,2]
tree1 = Bintree.BinTree()
tree2 = Bintree.BinTree()
tree1.CreateTree(root1)
tree2.CreateTree(root2)

a = Solution()
print(a.getAllElements(tree1.root, tree2.root))