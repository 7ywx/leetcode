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
        print(taskNum,workerNum)

tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
soulution = Solution()
soulution.maxTaskAssign(tasks, workers, pills, strength)
# @lc code=end
