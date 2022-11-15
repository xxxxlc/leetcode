
# 给你一个 值互不相同 的二叉树的根节点 root 。

# 在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。

# 返回每一层按 严格递增顺序 排序所需的最少操作数目。

# 节点的 层数 是该节点和根节点之间的路径的边数。

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0

        q = [root]

        while(q):
            
            array = []
            size = len(q)
            for i in range(size):
                cur = q.pop(0)
                array.append(cur.val)

                if cur.left is not None: q.append(cur.left)
                if cur.right is not None: q.append(cur.right)
            
            ans += self.minSwap(array)
        
        return ans



    def minSwap(self, nums):
        mp = {}
        sortNums = sorted(nums)

        for i in range(len(sortNums)):
            mp[sortNums[i]] = i
        
        loops = 0
        flags = [False] * len(sortNums)

        for i in range(len(sortNums)):
            if not flags[i]:
                j = i

                while(not flags[j]):
                    flags[j] = True

                    j = mp[nums[j]]
                loops += 1
        
        return len(nums) - loops


nums = [1, 2, 5, 4, 3]
a = Solution()

print(a.minSwap(nums))

