#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (52.01%)
# Likes:    1006
# Dislikes: 0
# Total Accepted:    306K
# Total Submissions: 588.4K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend]
# 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
# xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
#
#
# 示例 1：
#
#
# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。
#
# 示例 2：
#
#
# 输入：points = [[1,2],[3,4],[5,6],[7,8]]
# 输出：4
# 解释：每个气球需要射出一支箭，总共需要4支箭。
#
# 示例 3：
#
#
# 输入：points = [[1,2],[2,3],[3,4],[4,5]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# - 在x = 2处发射箭，击破气球[1,2]和[2,3]。
# - 在x = 4处射出箭，击破气球[3,4]和[4,5]。
#
#
#
#
#
# 提示:
#
#
# 1 <= points.length <= 10^5
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1
#
#
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if not points:
        #     return 0

        # points.sort(key=lambda balloon: balloon[1])
        # pos = points[0][1]
        # ans = 1
        # for balloon in points:
        #     if balloon[0] > pos:
        #         pos = balloon[1]
        #         ans += 1

        # return ans

        points = sorted(points, key=lambda x: x[0])
        n = len(points)
        i = 0
        interPoints = []
        while i < n:
            start, end = points[i]
            j = i + 1
            while j < n and points[j][0] >= start and points[j][0] <= end:
                start = max(start, points[j][0])
                end = min(end, points[j][1])
                j += 1
            interPoints.append([start, end])
            i = j

        return len(interPoints)


        # a = points
        # ansList = []
        # def dfs(points):
        #     if len(points) == 0:
        #         return 0
        #     ans = 0
        #     points.sort()
        #     hashmap = defaultdict(set)
        #     maxBoom = -1
        #     maxBooomList = []
        #     for i in range(len(points)):
        #         if hashmap[points[i][0]] is not None:
        #             for j in range(0, i+1):
        #                 if points[j][1] >= points[i][0]:
        #                     hashmap[points[i][0]].add(j)
        #                     if hashmap[points[i][0]].__len__() > maxBoom:
        #                         maxBoom = hashmap[points[i][0]].__len__()
        #         if hashmap[points[i][1]] is not None:
        #             j = 0
        #             while j < len(points) and points[j][0] <= points[i][1]:
        #                 if points[j][1] >= points[i][1]:
        #                     hashmap[points[i][1]].add(j)
        #                     if hashmap[points[i][1]].__len__() > maxBoom:
        #                         maxBoom = hashmap[points[i][1]].__len__()
        #                 j += 1
        #     print(hashmap)
        #     print(maxBoom)
        #     for k, v in hashmap.items():
        #         if v.__len__() == maxBoom:
        #             maxBooomList.append(k)
        #     print(maxBooomList)

        #     if all(len(value) == 1 for value in hashmap.values()):
        #         ans += len(hashmap)
        #         return ans

        #     for i in range(len(maxBooomList)):
        #         pointsNext = [points[_] for _ in range(len(points)) if _ not in hashmap[maxBooomList[i]]]
        #         ans += 1
        #         Next = dfs(pointsNext)
        #         ansList.append(ans + Next)
        #         ans = 0
        # dfs(points)
        # print(f"ansList:{ansList}")
        # return min(ansList)

        # def fms()
# @lc code=end
print(Solution.findMinArrowShots(Solution,[[10,16],[2,8],[1,6],[7,12]]))
