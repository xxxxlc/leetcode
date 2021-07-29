# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

# from leetcode.LinkedList.List import ListNode
import List

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = List.ListNode()
        pre = head
        while(l1 and l2):
            if l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            
            if head.val ==  None:
                head.val = val
            else:
                node = List.ListNode()
                node.val = val
                pre.next = node
                pre = node
        
        if l1 == None:
            pre.next = l2
        elif l2 == None:
            pre.next = l1

        return head


l1_element = [1,2,4]
l2_element = [1,3,4]
l1 = List.LinkedList()
l1.CreateLinkedList1(l1_element)
l2 = List.LinkedList()
l2.CreateLinkedList1(l2_element)

a = Solution()
result = a.mergeTwoLists(l1.head, l2.head)
l2.print_out(result)
