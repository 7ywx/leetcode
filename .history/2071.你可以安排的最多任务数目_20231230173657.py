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
        # 排序任务和工人的力量值
        tasks.sort()
        workers.sort()

        # 创建一个二维数组 dp，其中 dp[i][j] 表示前 i 个任务和前 j 个工人的最大完成任务数
        dp = [[0] * (len(workers) + 1) for _ in range(len(tasks) + 1)]
        print(dp)

        for i in range(1, len(tasks) + 1):
            for j in range(1, len(workers) + 1):
                # 不使用药丸，当前工人无法完成当前任务
                dp[i][j] = dp[i - 1][j]
                print(dp)

                # 使用药丸，当前工人可以完成当前任务
                if tasks[i - 1] <= workers[j - 1] + strength:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        # 返回最大完成任务数
        print(max(dp[-1]))
        return max(dp[-1])
        # tasks.sort()
        # workers.sort()

        # n, m = len(tasks), len(workers)

        # # dp[i][j] represents the maximum tasks that can be completed
        # # using the first i tasks and first j workers
        # dp = [[0] * (m + 1) for _ in range(n + 1)]

        # for i in range(1, n + 1):
        #     for j in range(1, m + 1):
        #         # If the j-th worker can handle the i-th task
        #         if workers[j - 1] >= tasks[i - 1]:
        #             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + 1)
        #         else:
        #             dp[i][j] = dp[i][j - 1]

        # # Add extra pills to increase the strength of workers if needed
        # for j in range(m + 1):
        #     while pills > 0 and j < m and workers[j] < tasks[n - 1]:
        #         workers[j] += strength
        #         pills -= 1
        #         j += 1
        # print(dp[n][m])
        # return dp[n][m]
    #     tasks.sort()  # 对任务列表进行排序
    #     workers.sort()  # 对工人列表进行排序
    #     completed_tasks = 0  # 已完成的任务数初始化为0
    #     for task in tasks:  # 遍历任务列表
    #         worker_index = self.find_worker(workers, task)  # 查找是否有与任务匹配的工人
    #         if worker_index is not None:  # 如果找到匹配的工人
    #             completed_tasks += 1  # 已完成的任务数加1
    #             workers.pop(worker_index)  # 移除该工人
    #         elif pills > 0 and workers:  # 如果没有匹配的工人且有足够的药丸和工人
    #             # 使用一颗药丸来增加最弱工人的力量
    #             workers[0] += strength
    #             pills -= 1
    #             #completed_tasks += 1  # 已完成的任务数加1
    #         else:
    #             break  # 没有更多的工人或药丸可供使用
    #     print(completed_tasks)  # 打印已完成的任务数
    #     return completed_tasks  # 返回已完成的任务数

    # def find_worker(self, workers: List[int], task: int) -> int:
    #     for i, worker_strength in enumerate(workers):
    #         if worker_strength >= task:
    #             return i
    #     return None

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
soulution.maxTaskAssign(tasks, workers, pills, strength)
#soulution.maxTaskAssign([5,4], [0,0,0], 1, 5)
# @lc code=end
