# 给你一个链表的头节点 head 。

# 对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。

# 返回修改后链表的头节点 head 。

class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []

        cur = head

        while(cur is not None):
            arr.append(cur.val)
            cur = cur.next
        
        removeIdx = []

        n = len(arr)
        temp = 0
        for i in range(n - 1, -1, -1):
            if arr[i] < temp:
                removeIdx.append(i)
                continue
            else:
                temp = arr[i]
        

        j = 0

        cur = head
        pre = None

        newHead = head

        while(len(removeIdx) > 0):
            if j == removeIdx[-1]:
                removeIdx.pop()

                if cur == newHead:
                    newHead = cur.next
                
                    cur = cur.next
                    pre = None

                else:
                    pre.next = cur.next
                    cur = cur.next
            else:
                pre = cur
                cur = cur.next

            j += 1
        
        return newHead
            

                
