# 完全二叉树是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

# 设计一个用完全二叉树初始化的数据结构 CBTInserter，它支持以下几种操作：

# CBTInserter(TreeNode root) 使用头节点为 root 的给定树初始化该数据结构；
# CBTInserter.insert(int v)  向树中插入一个新节点，节点类型为 TreeNode，值为 v 。使树保持完全二叉树的状态，并返回插入的新节点的父节点的值；
# CBTInserter.get_root() 将返回树的头节点。

from typing import Collection
import Bintree
from Bintree import TreeNode

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.dqueue = []
        q = []
        q.append(root)

        while(q):
            node = q.pop(0)
            if node.left == None or node.right == None:
                self.dqueue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.dqueue[0]
        self.dqueue.append(TreeNode(v))
        if node.left == None:
            node.left = self.dqueue[-1]
        else:
            node.right = self.dqueue[-1]
            self.dqueue.pop[0]
        
        return node.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root