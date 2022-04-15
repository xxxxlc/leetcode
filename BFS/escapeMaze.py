# 某解密游戏中，有一个 N*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 (n-1,m-1) 位置。迷宫变化规律记录于 maze 中，maze[i] 表示 i 时刻迷宫的地形状态，"." 表示可通行空地，"#" 表示陷阱。

# 地形图初始状态记作 maze[0]，此时小力位于起点 (0,0)。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。

# 小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：

# 临时消除术：将指定位置在下一个时刻变为空地；
# 永久消除术：将指定位置永久变为空地。
# 请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？

# 注意： 输入数据保证起点和终点在所有时刻均为空地。


from functools import lru_cache


class Solution(object):
    def escapeMaze(self, maze):
        """
        :type maze: List[List[str]]
        :rtype: bool
        """
        T, m, n = len(maze), len(maze[0]), len(maze[0][0])

        memo = set() # 或者：@lru_cache()
        def dfs(i, j, t, r1, r2):
            if t == T-1:
                if i == m - 1 and j == n - 1:
                    return True
                return False
            if i == m-1 and j == n-1:
                return True
            if (i, j, t, r1, r2) in memo:
                return False
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0), (0, 0)]:
                ii, jj = i+di, j+dj
                if not (0 <= ii < m and 0 <= jj < n):
                    continue
                if maze[t+1][ii][jj] == '.':
                    if dfs(ii, jj, t+1, r1, r2):
                        return True
                elif r1 == 0 and r2 == 0:
                    continue
                else:
                    if r1 > 0:
                        if dfs(ii, jj, t+1, 0, r2):
                            return True
                    if r2 > 0:
                        for k in range(t+1, T):
                            if dfs(ii, jj, k, r1, 0):
                                return True
            memo.add((i, j, t, r1, r2))
            return False
        
        return dfs(0, 0, 0, 1, 1) 

        




maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]

a = Solution()
print(a.escapeMaze(maze))