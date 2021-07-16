# 请判断一个链表是否为回文链表。

import List

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = List.ListNode()
        fast = List.ListNode()
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        if fast != None:
            slow = slow.next
        
        left = head
        right = self.reverse(slow)


        while(right):
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        
        return True

        


    def reverse(self, head):
        pre = None
        cur = head
        while(cur):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        return pre


head = [1,2,2,1]
list1 = List.LinkedList()
list1.CreateLinkedList1(head)

a = Solution()
k = 2
# print(a.isPalindrome(list1.head))
head = a.isPalindrome(list1.head)
print(head)
