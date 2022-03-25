# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 

import List

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        while(head.next and head.val == val):
            head = head.next 
        
        if not head:
            return head
        cur = head.next
        pre = head
        while(cur):
            if cur.val == val:
                pre.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                pre = pre.next
        
        return head

s = [1,2,6,3,4,5,6]
val = 6
l1 = List.LinkedList()
l1.CreateLinkedList1(s)

a = Solution()
res = a.removeElements(l1.head, val)
l1.print_out(res)
