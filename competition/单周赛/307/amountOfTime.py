# 给你一棵二叉树的根节点 root ，二叉树中节点的值 互不相同 。另给你一个整数 start 。在第 0 分钟，感染 将会从值为 start 的节点开始爆发。

# 每分钟，如果节点满足以下全部条件，就会被感染：

# 节点此前还没有感染。
# 节点与一个已感染节点相邻。
# 返回感染整棵树需要的分钟数。

import Bintree

class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        self.graph = dict()

        self.buildGraph(root, None)

        q = [start]
        time = 0
        visited = set()
        visited.add(start)

        while(q):
            size = len(q)

            for i in range(size):
                curNode = q.pop(0)

                for neightborNode in self.graph[curNode]:
                    if neightborNode not in visited:
                        visited.add(neightborNode)
                        q.append(neightborNode)
            
            time += 1
        
        return time - 1


    def buildGraph(self, node, fatherNode):
        if node is None:
            return
        if fatherNode is None:
            self.graph[node.val] = []
        else:
            self.graph[node.val] = [fatherNode.val]
            self.graph[fatherNode.val].append(node.val)
        
        self.buildGraph(node.left, node)
        self.buildGraph(node.right, node)



node = [1]
start = 1
tree = Bintree.BinTree()
tree.CreateTree(node)
tree.horizontallyshow(tree.root, tree.root)

a = Solution()
print(a.amountOfTime(tree.root, start))