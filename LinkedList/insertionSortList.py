# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。

# 插入排序 算法的步骤:

# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

# 对链表进行插入排序。

import List

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        cur = head
        newHead = head

        while (cur.next):
            nxt = cur.next
            if nxt.val >= cur.val:
                cur = nxt
                continue
            else:
                cur.next = nxt.next
                p = newHead
                pre = None
                while (p.val < nxt.val):
                    pre = p
                    p = p.next
                if pre is None:
                    nxt.next = newHead
                    newHead = nxt
                else:
                    pre.next = nxt
                    nxt.next = p
        
        return newHead
                



head = [-1,5,3,4,0]
l1 = List.LinkedList()
l1.CreateLinkedList1(head)

a = Solution()
ans = a.insertionSortList(l1.head)
l1.print_out(ans)