# 给定一个整数数组 asteroids，表示在同一行的行星。

# 对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

# 找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        i = 0

        while(i < len(asteroids) - 1):
            if asteroids[i] > 0 and asteroids[i + 1] < 0:
                if asteroids[i] == -asteroids[i + 1]:
                    asteroids.pop(i)
                    asteroids.pop(i)
                    if i > 0:
                        i = i - 1
                elif abs(asteroids[i]) > abs(asteroids[i + 1]):
                    asteroids.pop(i + 1)
                else:
                    asteroids.pop(i)
                    if i > 0:
                        i = i - 1
            else:
                i += 1

        return asteroids

                
asteroids = [1,-1,-2,1]

a = Solution()
print(a.asteroidCollision(asteroids))