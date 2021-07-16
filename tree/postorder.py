class Solution(object):
    res = []
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.postorder_find(root)
        return self.res
    
    def postorder_find(self, root):
        if root == None:
            return

        for child in root.children:
            self.postorder_find(child)
            
        self.res.append(root.val)