# 给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

# 请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

# mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
# maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
# 返回数组 answer 。


class Solution(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        self.array = []

        self.search(root)

        ans = []

        for i in range(len(queries)):
            if queries[i] > self.array[-1]:
                ans.append([self.array[-1], -1])
                continue

            # for j in range(len(self.array)):
            #     if queries[i] == self.array[j]:
            #         ans.append([self.array[j], self.array[j]])
            #         break
            #     if queries[i] < self.array[j]:
            #         if j == 0:
            #             ans.append([-1, self.array[j]])
            #             break
            #         ans.append([self.array[j - 1], self.array[j]])
            #         break
            l = 0
            r = len(self.array)

            isfind = False

            while (l < r):
                mid = l + (r - l) // 2
                if queries[i] == self.array[mid]:
                    ans.append[[self.array[mid], self.array[mid]]]
                    isfind = True
                    break
                elif queries[i] < self.array[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            if not isfind:
                if l == 0:
                    ans.append([-1, self.array[l]])
                elif l == len(self.array):
                    ans.append([self.array[l], -1])
                else:
                    ans.append([self.array[l-1], self.array[l]])


        return ans
    
    def search(self, root):
        if (root is None): return 


        self.search(root.left)

        self.array.append(root.val)

        self.search(root.right)


        





 