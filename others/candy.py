# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

# 你需要按照以下要求，帮助老师给这些孩子分发糖果：

# 每个孩子至少分配到 1 个糖果。
# 相邻的孩子中，评分高的孩子必须获得更多的糖果。
# 那么这样下来，老师至少需要准备多少颗糖果呢？

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        number_children = len(ratings)
        candy_list = [1] * number_children
        for children in range(number_children - 1):
            if ratings[children + 1] > ratings[children]:
                candy_list[children + 1] += candy_list[children]
        for children in range(number_children-2, -1, -1):
            if ratings[children] > ratings[children + 1]:
                candy_list[children] = max(candy_list[children + 1] + 1, candy_list[children])
        print(sum(candy_list))
        return candy_list

a = Solution()
ratings = [1,2,87,87,87,2,1]
print(a.candy(ratings))
