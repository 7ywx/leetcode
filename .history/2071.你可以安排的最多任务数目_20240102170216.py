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
        n, m = len(tasks), len(workers)  # 获取任务列表和工人列表的长度
        tasks.sort()  # 对任务列表进行升序排序
        workers.sort()  # 对工人列表进行升序排序

        def check(mid: int) -> bool:  # 定义一个检查函数，用于判是否能完成mid个任务
            p = pills  # 初始化药丸数量
            ws = SortedList(workers[m - mid:])  # 后m-mid个工人的有序列表
            for i in range(mid - 1, -1, -1):  # 从大到小枚举每一个任务
                # 如果有序集合中最大的元素大于等于 tasks[i]
                if ws[-1] >= tasks[i]:  # 如果有序集合中最大的工人力量大于等于当前任务需求
                    ws.pop()  # 移除力量最大的工人
                else:
                    if p == 0:  # 如果没有剩余的药丸
                        return False  # 返回False，表示无法满足任务需求
                    rep = ws.bisect_left(tasks[i] - strength)  # 使用二分查找找到离tasks[i] - strength最近的元素的索引
                    if rep == len(ws):  # 如果查找到的索引已经达到有序集合的末尾
                        return False  # 返回False，表示无法满足任务需求
                    p -= 1  # 药丸数量减1
                    ws.pop(rep)  # 移除指定索引处的元素

            return True  # 返回True，表示能满足任务需求

        left, right, ans = 1, min(m, n), 0  # 初始化左边界、右边界和答案变量
        while left <= right:  # 当左边界小于等于右边界时循环
            mid = (left + right) // 2  # 计算左边界和右边界的中间值
            if check(mid):  # 如果中间值满足任务需求
                ans = mid  # 更新答案变量
                left = mid + 1  # 更新左边界
            else:
                right = mid - 1  # 更新右边界

        return ans  # 返回答案


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
