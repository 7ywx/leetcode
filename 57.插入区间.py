#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode.cn/problems/insert-interval/description/
#
# algorithms
# Medium (42.68%)
# Likes:    924
# Dislikes: 0
# Total Accepted:    228.4K
# Total Submissions: 535.2K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给你一个 无重叠的 ，按照区间起始端点排序的区间列表 intervals，其中 intervals[i] = [starti, endi] 表示第 i
# 个区间的开始和结束，并且 intervals 按照 starti 升序排列。同样给定一个区间 newInterval = [start, end]
# 表示另一个区间的开始和结束。
#
# 在 intervals 中插入区间 newInterval，使得 intervals 依然按照 starti
# 升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。
#
# 返回插入之后的 intervals。
#
# 注意 你不需要原地修改 intervals。你可以创建一个新数组然后返回它。
#
#
#
# 示例 1：
#
#
# 输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出：[[1,5],[6,9]]
#
#
# 示例 2：
#
#
# 输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出：[[1,2],[3,10],[12,16]]
# 解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#
#
#
# 提示：
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals 根据 starti 按 升序 排列
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#
from typing import List
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #
        res = []
        i = 0
        length = len(intervals)

        # 当前遍历的是左边的，不重叠的区间
        while i < length and intervals[i][1] < newInterval[0]: # 等价于 not newInterval[0] <= intervals[i][1]
            res.append(intervals[i])
            i += 1

        # 当前遍历是有重叠的区间
        while i < length and intervals[i][0] <= newInterval[1]: # 等价于 not newInterval[1] < intervals[i][0]
            newInterval[0] = min(newInterval[0], intervals[i][0])  # 左端取较小者，更新给新区间的左端
            newInterval[1] = max(newInterval[1], intervals[i][1])  # 右端取较大者，更新给新区间的右端
            i += 1
        res.append(newInterval)  # 循环结束后，新区间为合并后的区间，推入res

        # 在右边，没重叠的区间
        while i < length:
            res.append(intervals[i])
            i += 1

        return res

        # i = 0
        # n = len(intervals)
        # if n == 0:
        #     return [newInterval]
        # while i < n and not newInterval[0] <= intervals[i][1]:
        #     i += 1
        # left = i
        # while i < n and not newInterval[1] < intervals[i][0]:
        #     i += 1
        # right = i
        # # print(left, right)
        # if left == right: return intervals[:left] + [newInterval] + intervals[right:]
        # return intervals[:left] + [[min(newInterval[0], intervals[left][0]), max(newInterval[1], intervals[right-1][1])]] + intervals[right:]

        # 将新的区间插入到数组中，排序，合并
        intervals.append(newInterval)
        intervals.sort() # intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        l = len(intervals)
        for i in range(1, l):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged

# @lc code=end
print(Solution().insert([[1,3],[6,9]], [2,5]))
