# 给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

# 第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

# 请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

# 你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。


import List

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        if head.next is None:
            return head

        if head.next.next is None:
            return head

        count = 1
        cur = head
        pre = None
        n = 1
        
        while (cur.next):
            cur = cur.next
            n += 1
        tail = cur

        cur = head

        while (count <= n):
            if count % 2 == 0:
                pre.next = cur.next
                tail.next = cur
                tail = tail.next

                cur = cur.next
                tail.next = None
            else:
                pre = cur
                cur = cur.next
            count += 1

        return head


head = [1,2,3,4,5]
l1 = List.LinkedList()

l1.CreateLinkedList1(head)

a = Solution()
head1 = a.oddEvenList(l1.head)
l1.print_out(head1)