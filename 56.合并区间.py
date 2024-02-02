#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (49.72%)
# Likes:    2228
# Dislikes: 0
# Total Accepted:    778.6K
# Total Submissions: 1.6M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
# 示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
# 提示：
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 0
        intervals_len = len(intervals)
        while i < intervals_len - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][1] < intervals[i + 1][1]: # intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                    intervals[i][1] = intervals[i + 1][1]
                intervals.pop(i + 1) # remove(x)：从列表中移除第一个出现的指定值的元素
                intervals_len -= 1
            else:
                i += 1
        # print(intervals)
        return intervals
# @lc code=end
solution = Solution()
solution.merge([[1,3],[2,6],[8,10],[15,18]])
