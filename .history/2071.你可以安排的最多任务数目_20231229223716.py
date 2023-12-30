#
# @lc app=leetcode.cn id=2071 lang=python3
#
# [2071] 你可以安排的最多任务数目
#

# @lc code=start
from typing import List
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        taskNum=len(tasks)
        workerNum=len(workers)
        minNum=min(taskNum,workerNum)
        print(minNum)
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n = len(tasks)
        m = len(workers)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = pills
        for i in range(n):
            for j in range(m + 1):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                if workers[j] >= tasks[i]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] - pills + 1)
        print(dp[n][m])
        return dp[n][m]

tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
soulution = Solution()
soulution.maxTaskAssign(tasks, workers, pills, strength)
# @lc code=end
