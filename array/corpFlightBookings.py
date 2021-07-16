# 这里有 n 个航班，它们分别从 1 到 n 进行编号。

# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

# 请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。


class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0]*n
        for i in range(0, len(bookings)):
            res[bookings[i][0] - 1] += bookings[i][2]
            if bookings[i][1] >= len(res):
                continue
            res[bookings[i][1]] -= bookings[i][2]
            print(res)
        
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        
        return res



a = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(a.corpFlightBookings(bookings, n))