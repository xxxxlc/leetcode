# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。

import List

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        l3 = self.addList(l1, l2)

        return self.reverseList(l3)

    def addList(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1

        if l1.val == 0 and l1.next is None:
            return l2
        if l2.val == 0 and l2.next is None:
            return l1

        while(l1 and l2):
            l1.val = l1.val + l2.val
            if l1.val > 9:
                l1.val = l1.val % 10
                if l1.next:
                    l1.next.val += 1
                else:
                    node = List.ListNode(1)
                    l1.next = node
            pre = l1
            l1 = l1.next
            l2 = l2.next
        
        if not l1:
            pre.next = l2
        while(pre):
            if pre.val > 9:
                pre.val = pre.val % 10
                if pre.next:
                    pre.next.val = pre.next.val + 1
                else:
                    node = List.ListNode(1)
                    pre.next = node
            pre = pre.next

        return head

    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        p = head
        while(p.next):
            p = p.next
        tail = p
        pre = None
        cur = head
        nxt = head
        while(pre != tail):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre



head1 = [7,2,4,3]
head2 = [5,6,4]

l1 = List.LinkedList()
l2 = List.LinkedList()

l1.CreateLinkedList1(head1)
l2.CreateLinkedList1(head2)

a = Solution()
head3 = a.addTwoNumbers(l1.head, l2.head)
l1.print_out(head3)