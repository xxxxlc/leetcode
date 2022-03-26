# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

import List


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        slow = head
        node = List.ListNode()
        node.next = head
        pre = node
        fast = head.next

        isduplicates = False

        while (True):
            if not fast:
                if isduplicates:
                    pre.next = None
                break
            if slow.val != fast.val:
                if not isduplicates:
                    pre = slow
                    slow = slow.next
                else:
                    isduplicates = False
                slow.val = fast.val

            else:
                isduplicates = True 
            
            fast = fast.next

        if slow:
            slow.next = None
        
        return node.next

s = [1,2,3,4,5]

l1 = List.LinkedList()
l1.CreateLinkedList1(s)

a = Solution()
head = a.deleteDuplicates(l1.head)
l1.print_out(head)

