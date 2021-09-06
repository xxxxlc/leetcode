# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表

import List

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heads = lists[:]
        ansHead = None
        ans = None
        while(len(heads) > 0):
            for head in heads[:]:
                if head is None:
                    heads.remove(head)
            
            if len(heads) == 0:
                break
            
            min = float('inf')
            for head in heads:
                if head.val < min:
                    min = head.val
                    pre = head
            heads.remove(pre)
            heads.append(pre.next)

            if ans is not None:
                ans.next = pre
                ans = ans.next
            else:
                ans = pre
                ansHead = ans
        
        return ansHead



lists = [[],[],[]]
heads = []

for list in lists:
    l = List.LinkedList()
    l.CreateLinkedList1(list)
    heads.append(l.head)

a = Solution()
head = a.mergeKLists(heads)
l.print_out(head)