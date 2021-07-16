


import Bintree
class Solution(object):
    ans = []
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        height = self.gettreehight(root)
        self.ans = []
        ans_lev = []
        width = pow(2, height) - 1
        for i in range(0, width):
            ans_lev.append("")
        self.DFS(root, ans_lev, 1, 0, width-1)
        return self.ans

    def DFS(self, root, ans_lev, depth, lo, hi):
        if root == None:
            return
        
        if len(self.ans) < depth:
            self.ans.append(ans_lev[:])
        
        index = int((lo + hi) / 2)

        self.ans[depth - 1][index] = str(root.val)


        self.DFS(root.left, ans_lev, depth+1, lo, index-1)
        self.DFS(root.right, ans_lev, depth+1, index+1, hi)


    def gettreehight(self, root):
        if root == None:
            return 0
        
        return max(self.gettreehight(root.left), self.gettreehight(root.right)) + 1


root = [1,2,3,None,4]
tree = Bintree.BinTree()
tree.CreateTree(root)

a = Solution()
print(a.printTree(tree.root))
