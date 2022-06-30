# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        q = []
        visited = {}
        visited[node.val] = Node(node.val, None)

        q.append(node)
        while (q):
            curNode = q.pop(0)

            for neighbor in curNode.neighbors:
                if neighbor.val not in visited.keys():
                    newNode = Node(neighbor.val, None)
                    visited[neighbor.val] = newNode
                    visited[curNode.val].neighbors.append(newNode)
                    q.append(neighbor)
                else:
                    visited[curNode.val].neighbors.append(visited[neighbor.val])
    
        return visited[node.val]
