# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。

# 如果有两个中间结点，则返回第二个中间结点。

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head

        while(fast and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        return slow