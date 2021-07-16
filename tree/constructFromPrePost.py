# 返回与给定的前序和后序遍历匹配的任何二叉树。

# pre 和 post 遍历中的值是不同的正整数

import Bintree

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        
        root = Bintree.TreeNode(pre[0])
        if len(pre) == 1:
            return root
        post_index = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:post_index + 2], post[0:post_index + 1])
        root.right = self.constructFromPrePost(pre[post_index + 2:], post[post_index + 1:len(post) - 1])


        return root



pre = [9,10,6,1,4,2,3,7,8,5]

post = [10,4,1,7,5,8,3,2,6,9]

a = Solution()
root = a.constructFromPrePost(pre, post)

tree = Bintree.BinTree()

tree.horizontallyshow(root, root)