#
# @lc app=leetcode.cn id=2071 lang=python3
#
# [2071] 你可以安排的最多任务数目
#

# @lc code=start
from typing import List
from typing import List
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        completed_tasks = 0
        for task in tasks:
            worker_index = self.find_worker(workers, task)
            if worker_index is not None:
                completed_tasks += 1
                workers.pop(worker_index)
            elif pills > 0 and workers:
                # Use a pill to increase the strength of the weakest worker
                workers[0] += strength
                pills -= 1
                completed_tasks += 1
            else:
                break  # No more workers or pills available
        print(completed_tasks)
        return completed_tasks

    def find_worker(self, workers: List[int], task: int) -> int:
        for i, worker_strength in enumerate(workers):
            if worker_strength >= task:
                return i
        return None

        # n = len(tasks)
        # m = len(workers)
        # dp = [[0] * (m + 1) for _ in range(n )] #列表表达式
        # matrix = [[i + j for j in range(2, 4)] for i in range(1, 4)]
        # print(dp)
        # dp[0][0] = pills
        # for i in range(n):
        #     for j in range(m + 1):
        #         dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        #         if workers[j] >= tasks[i]:
        #             dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] - pills + 1)
        # return dp[n][m]

tasks = [3, 2, 1]
workers = [0, 3, 3]
pills = 1
strength = 1
soulution = Solution()
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
couples = [(x, y) for x in list1 for y in list2]
# print(couples)   输出 [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
#soulution.maxTaskAssign(tasks, workers, pills, strength)
soulution.maxTaskAssign([5,4], [0,0,0], 1, 5)
# @lc code=end
def max_tasks_completed(tasks, workers, pills, strength):
    tasks.sort()
    workers.sort()

    completed_tasks = 0
    for task in tasks:
        worker_index = find_worker(workers, task)

        if worker_index is not None:
            completed_tasks += 1
            workers.pop(worker_index)
        elif pills > 0 and workers:
            # Use a pill to increase the strength of the weakest worker
            workers[0] += strength
            pills -= 1
            completed_tasks += 1
        else:
            break  # No more workers or pills available

    return completed_tasks

def find_worker(workers, task):
    for i, worker_strength in enumerate(workers):
        if worker_strength >= task:
            return i
    return None

# Example usage
# tasks = [3, 7, 2]
# workers = [5, 10, 6]
# pills = 2
# strength = 3

# result = max_tasks_completed(tasks, workers, pills, strength)
# print(result)
