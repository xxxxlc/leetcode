# 给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

# 每个节点都有 0 个或是 2 个子节点。
# 数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
# 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
# 在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

import Bintree 
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = [float('inf'),]
        mct = 0

        for i in range(0, len(arr)):
            while(arr[i] >= stack[-1]):
                mct += stack.pop() * min(arr[i], stack[-1])
            stack.append(arr[i])
        
        while(len(stack) > 2):
            mct += stack.pop() * stack[-1]
        
        return mct
        

    



arr = [6,2,4]
a = Solution()
print(a.mctFromLeafValues(arr))
