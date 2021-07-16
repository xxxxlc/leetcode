# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

import List

class Solution(object):
    successor = List.ListNode()
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            return self.reverseN(head, right)
        
        head.next =  self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head
        
        last = self.reverseN(head.next, n - 1)

        head.next.next = head

        head.next = self.successor

        return last

head = [1,2,3,4,5]
list1 = List.LinkedList()
list1.CreateLinkedList1(head)
left = 2
right = 4

a = Solution()
print(list1.print_out(a.reverseBetween(list1.head, left, right)))

