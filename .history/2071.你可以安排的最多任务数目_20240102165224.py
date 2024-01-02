#
# @lc app=leetcode.cn id=2071 lang=python3
#
# [2071] 你可以安排的最多任务数目
#

# @lc code=start
from typing import List
class Solution:
    def find_worker(self, workers: List[int], task: int, strength: int) -> int:
        for i, worker_strength in enumerate(workers):
            if worker_strength+strength >= task:
                return i
        return None
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        
        # # # 排序任务和工人的力量值
        # # tasks.sort(reverse=True)
        # # workers.sort()
        # tasks.sort()  # 对任务列表进行排序
        # workers.sort()  # 对工人列表进行排序
        # completed_tasks = 0  # 已完成的任务数初始化为0
        # for task in tasks:  # 遍历任务列表
        #     worker_index0 = self.find_worker(workers, task, 0)  # 查找是否有与任务匹配的工人
        #     if worker_index0 is not None:  # 如果找到匹配的工人
        #         completed_tasks += 1  # 已完成的任务数加1
        #         workers.pop(worker_index0)  # 移除该工人
        #     elif pills > 0 and workers:  # 如果没有匹配的工人且有足够的药丸和工人
        #         # 使用一颗药丸来增加最弱工人的力量
        #         worker_indexs = self.find_worker(workers, task, strength)
        #         if worker_indexs is not None:  # 如果找到匹配的工人
        #             pills -= 1
        #             completed_tasks += 1  # 已完成的任务数加1
        #             workers.pop(worker_indexs)  # 移除该工人
        # print(completed_tasks)  # 打印已完成的任务数
        # return completed_tasks  # 返回已完成的任务数


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
#soulution.maxTaskAssign([5,9,8,5,9], [1,6,4,2,6], 1, 5)
#soulution.maxTaskAssign([10,15,30], [0,10,10,10,10], 3, 10)
# @lc code=end
