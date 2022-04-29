# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。


import List

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        pre = List.ListNode()
        prenode = pre
        pre.next = head
        cur = head
        next = head.next
        while (cur and next):
            temp = next.next
            next.next = cur
            cur.next = temp
            pre.next = next

            if cur:
                pre = cur
                cur = cur.next
            if cur:
                next = cur.next
        return prenode.next

s1 = List.LinkedList()
nums = [1,2,3,4,5,6]
s1.CreateLinkedList1(nums)

a = Solution()
head = a.swapPairs(s1.head)
s1.print_out(head)