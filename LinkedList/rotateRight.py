#  给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

import List

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        length = 1
        cur = head
        while (cur.next != None):
            cur = cur.next
            length += 1

        k = k % length

        for i in range(0, k):
            cur = head
            while (cur.next.next != None):
                cur = cur.next
            nxt = cur.next
            cur.next = None
            nxt.next = head
            head = nxt
        return head
            

num = [1,2]
k = 2

l = List.LinkedList()
l.CreateLinkedList1(num)

a = Solution()
head = a.rotateRight(l.head, k)
l.print_out(head)