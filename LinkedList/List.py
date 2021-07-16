
class ListNode(object):
    def __init__(self, val=None, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre

class LinkedList(object):

    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None

    def CreateLinkedList1(self, lists):
        head = self.head
        for i in range(0, len(lists)):
            listnode = ListNode(lists[i])
            if head == None:
                head = listnode
                self.head = listnode

            else:
                head.next = listnode
                head = listnode
    
    def __str__(self):
        res = ''
        head = self.head
        while(head):
            res = res + str(head.val)
            head = head.next
        
        return res

    def print_out(self, head):
        while(head):
            print(head.val,end=' ')
            head = head.next
                
if __name__ == "__main__":
    a = [1,2,3,4,5]
    link_list = LinkedList()
    link_list.CreateLinkedList1(a)
    print(link_list)
    link_list.print_out(link_list.head)

    

