# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


import List

class Solution(object):
    def addTwoNumbers(self, l1, l2):
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

head1 = [2,4,3]
head2 = [5,6,4]

l1 = List.LinkedList()
l2 = List.LinkedList()

l1.CreateLinkedList1(head1)
l2.CreateLinkedList1(head2)

a = Solution()
head3 = a.addTwoNumbers(l1.head, l2.head)
l1.print_out(head3)