# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB

        while(p1 != p2):
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
            
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p1
