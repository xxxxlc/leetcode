# 给你一棵以 root 为根的二叉树和一个 head 为第一个节点的链表。

# 如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 head 为首的链表中每个节点的值，那么请你返回 True ，否则返回 False 。

# 一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

import sys
sys.path.append('D:\programming\leetcode\\')
print(sys.path)
import Bintree
from LinkedList import List

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        self.head = head
        return self.helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def helper(self, head, root):
        if head == None:
            return True
        
        if root == None:
            return False
        
        if root.val != head.val:
            return False
        
        return self.helper(head.next, root.left) or self.helper(head.next, root.right)
        



root = [2,None,2,None,2,None,1]
tree = Bintree.BinTree()
tree.CreateTree(root)
tree.horizontallyshow(tree.root, tree.root)

head = [2,2,1]
list = List.LinkedList()
list.CreateLinkedList1(head)

a = Solution()
print(a.isSubPath(list.head, tree.root))