#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode.cn/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.27%)
# Likes:    817
# Dislikes: 0
# Total Accepted:    148.1K
# Total Submissions: 288.8K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
#
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
#
#
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
#
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
#
# 示例 2：
#
#
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
#
#
# 示例 3：
#
#
# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] 仅为 0、1 或 2
#
#
#
from typing import List, Optional
import collections
def print_grid(grid: List[List[str]]) -> None:
    for i in grid:
        print(i)
    print()
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        根据给定的橘子存储网格grid模拟橘子腐烂过程，并计算所有新鲜橘子变为腐烂所需的时间（以分钟计）。

        参数:
        grid (List[List[int]]): 二维整数列表，表示橘子的状态。0代表空单元格，1代表新鲜橘子，2代表腐烂橘子。

        返回值:
        int: 所有新鲜橘子变为腐烂所需的最小时间（分钟）。若无法完成腐烂，则返回-1。

        实现逻辑:
        1. 遍历grid记录初始时腐烂和新鲜橘子的位置。
        2. 使用deque数据结构rot存储腐烂橘子位置，便于后续优先处理最近刚腐烂的橘子。
        3. 定义infect函数用于传播腐烂，当遍历到腐烂橘子时，将其相邻的新鲜橘子感染为腐烂橘子，并加入rot队列中。
        4. 主循环中不断进行腐烂传播，每轮传播后增加一分钟计数，直到没有新鲜橘子或者无腐烂橘子可以继续传播为止。
        """

        res = 0  # 初始化记录所需时间变量
        n = len(grid)
        m = len(grid[0])
        rot = collections.deque()  # 存储腐烂橘子坐标
        fresh = []  # 存储新鲜橘子坐标

        # 遍历grid记录腐烂和新鲜橘子的位置
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.append((i, j))
                elif grid[i][j] == 2:
                    rot.append((i, j))

        # 定义腐烂传播函数
        def infect(x, y):
            # 如果当前单元格是腐烂橘子，检查并感染相邻的新鲜橘子
            if grid[x][y] == 2:
                # 右侧邻居
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    rot.append((x - 1, y))
                    fresh.remove((x - 1, y))

                # 左侧邻居
                if x < n - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    rot.append((x + 1, y))
                    fresh.remove((x + 1, y))

                # 上方邻居
                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    rot.append((x, y - 1))
                    fresh.remove((x, y - 1))

                # 下方邻居
                if y < m - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    rot.append((x, y + 1))
                    fresh.remove((x, y + 1))

        # 开始腐烂传播主循环
        while fresh:
            for i in range(len(rot)):
                coordinate = rot.popleft()
                infect(coordinate[0], coordinate[1])  # 传播腐烂
            res += 1 # 增加1分钟
            if not rot:
                return -1  # 若当前腐烂橘子队列为空，则无法继续传播，返回-1
        return res  # 当所有新鲜橘子都已腐烂时，返回所需时间
# @lc code=end
solution = Solution()
print(solution.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
# print(solution.orangesRotting(grid = [[0,2]]))
# print(solution.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))
# print(solution.orangesRotting(grid = [[2,1,1],[1,1,1],[0,1,2]]))
