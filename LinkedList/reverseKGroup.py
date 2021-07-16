# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序

import List

class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        a = List.ListNode()
        a = head
        b = List.ListNode()
        b = head

        for i in range(0, k):
            if b == None:
                return head
            b = b.next
        
        new = self.reverseN(a, b)

        a.next = self.reverseKGroup(b, k)
        return new
    
    def reverseN(self, head, tail):
        pre = List.ListNode()
        cur = head
        nxt = head
        while(cur != tail):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre


head = [1,2,3,4,5]
list1 = List.LinkedList()
list1.CreateLinkedList1(head)

a = Solution()
k = 2
head = a.reverseKGroup(list1.head, 2)
list1.print_out(head)