# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。


import List

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        for i in range(0, n):
            fast = fast.next
        
        if fast is None:
            return head.next
        slow = head

        while(fast.next):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head




head = [1,2,3,4,5]
n = 2

l1 = List.LinkedList()
l1.CreateLinkedList1(head)

a = Solution()
head = a.removeNthFromEnd(l1.head, n)
l1.print_out(head)