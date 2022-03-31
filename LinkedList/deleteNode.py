# 请编写一个函数，用于 删除单链表中某个特定节点 。在设计函数时需要注意，你无法访问链表的头节点 head ，只能直接访问 要被删除的节点 。

# 题目数据保证需要删除的节点 不是末尾节点 。

import List

class Solution(object):
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        


head = [4,5,1,9]
node = 5

s1 = List.LinkedList()
s1.CreateLinkedList1(head)

a = Solution()
print(a.deleteNode(s1.head, node))

s1.print_out(s1.head)

