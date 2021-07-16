# 给你一个链表和一个特定值 x ，请你对链表进行分隔，使得所有小于 x 的节点都出现在大于或等于 x 的节点之前。

# 你应当保留两个分区中每个节点的初始相对位置。

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class SLinkedList(object):
    def __init__(self):
        self.headval = None
    
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.val,end=' ')
            printval = printval.next
        print()    
    def AtBegining(self, new):
        Newnode = ListNode(new)
        Newnode.next = self.headval
        self.headval = Newnode

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        linked_max = ListNode(0)
        head_max = linked_max
        linked_min = ListNode(0)
        head_min = linked_min
        tail_min = None
        while head is not None:
            head_next = head.next
            if head.val >= x:
                linked_max.next = head
                linked_max = linked_max.next
                linked_max.next = None
            else:
                linked_min.next = head
                linked_min = linked_min.next
                tail_min = linked_min
                linked_min.next = None
            head = head_next
        
        if head_max.next is not None:
            head_max = head_max.next
        else:
            return head_min.next
        if head_min.next is not None:
            head_min = head_min.next
        else:
            return head_max
        tail_min.next = head_max

        # while head_max is not None:
        #     print(head_max.val,end=' ')
        #     head_max = head_max.next
        # print()  
        result = head_min
        while head_min is not None:
            print(head_min.val,end=' ')
            head_min = head_min.next
        print() 
        return result


a = Solution()
give_linkedlist = [1]
number = 0
linkedlist = SLinkedList()
linkedlist.headval = ListNode(give_linkedlist[len(give_linkedlist) - 1])

for index in range(len(give_linkedlist)-2,-1,-1):
    linkedlist.AtBegining(give_linkedlist[index])

linkedlist.listprint()

print(a.partition(linkedlist.headval, number))