# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

# 返回同样按升序排列的结果链表。

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while(fast != None):
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            
            fast = fast.next
        
        slow.next = None
        return head