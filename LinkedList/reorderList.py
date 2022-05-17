# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：

# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

import List

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        slow = fast = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        cur = head
        while (slow.next != None):
            pre = slow
            insertNode = slow.next
            while (insertNode.next != None):
                pre = insertNode
                insertNode = insertNode.next
            pre.next = None
            
            tmp = cur.next
            cur.next = insertNode
            cur.next.next = tmp
            cur = tmp
        
        return head
            


head = [1,2,3,4,5]
l1 = List.LinkedList()
l1.CreateLinkedList1(head)

a = Solution()
head1 = a.reorderList(l1.head)
l1.print_out(head1)