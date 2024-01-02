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
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            #  工人的有序集合
            ws = SortedList(workers[m - mid:])
            # 从大到小枚举每一个任务
            for i in range(mid - 1, -1, -1):
                # 如果有序集合中最大的元素大于等于 tasks[i]
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

作者：力扣官方题解
链接：https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/solutions/1101831/ni-ke-yi-an-pai-de-zui-duo-ren-wu-shu-mu-p7dm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
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
