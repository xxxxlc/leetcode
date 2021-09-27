# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表

import List

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sortfunc(head, None)
    
    def sortfunc(self, head, tail):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        
        slow = fast = head
        while(fast != tail):
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
            
        
        return self.merge(self.sortfunc(head, slow), self.sortfunc(slow, tail))
    
    def merge(self, head1, head2):
        dummyHead = List.ListNode(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        
        return dummyHead.next


head = [4,2,1,3]
l = List.LinkedList()
l.CreateLinkedList1(head)

a = Solution()
head = a.sortList(l.head)
l.print_out(head)