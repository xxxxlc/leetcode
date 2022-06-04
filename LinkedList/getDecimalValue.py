# 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

# 请你返回该链表所表示数字的 十进制值 。

import List


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """

        ans = 0
        cur = head
        while (cur != None):
            ans = ans * 2 + cur.val
            cur = cur.next
        return ans


nums = [1,0,1]
l1 = List.LinkedList()
l1.CreateLinkedList1(nums)

a = Solution()
print(a.getDecimalValue(l1.head))