from typing import List
#
# @lc app=leetcode.cn id=149 lang=python3
# @lcpr version=20002
#
# [149] 直线上最多的点数
#
# https://leetcode.cn/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (41.21%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    101.2K
# Total Submissions: 245.4K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
#
#
# 示例 2：
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
#
#
# 提示：
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# points 中的所有点 互不相同
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        hashmap = defaultdict(set)
        maxPoints = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if points[i][0] ==  points[j][0]:
                    hashmap[(float('inf'), points[i][0])].update([i, j])
                    maxPoints = max(maxPoints, len(hashmap[(float('inf'), points[i][0])]))
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    b = points[i][1] - k * points[i][0]
                    # if k == 0: k = 0
                    hashmap[(k, b)].update([i, j])
                    maxPoints = max(maxPoints, len(hashmap[(k, b)]))
            # 提前终止：如果当前点的最大点数已经超过了剩余点数的总和，可以提前终止计算。
            if maxPoints > len(points) // 2:
                return maxPoints
        return maxPoints

# @lc code=end



#
# @lcpr case=start
# [[1,1],[2,2],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]\n
# @lcpr case=end

#
