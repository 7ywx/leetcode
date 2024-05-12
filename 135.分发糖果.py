#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#
# https://leetcode.cn/problems/candy/description/
#
# algorithms
# Hard (48.92%)
# Likes:    1497
# Dislikes: 0
# Total Accepted:    314K
# Total Submissions: 642.2K
# Testcase Example:  '[1,0,2]'
#
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
#
#
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#
#
# 示例 1：
#
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
#
#
# 示例 2：
#
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# ⁠    第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
#
#
#
# 提示：
#
#
# n == ratings.length
# 1 <= n <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4
#
#
#
from typing import List
# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        根据学生的评分分配糖果。

        每个学生至少分配到一个糖果。如果一个学生比他的右边或者左边的学生评分高，
        他将分配到比右边或左边学生更多的糖果。计算需要分配的糖果总数。

        参数:
        ratings (List[int]): 学生的评分列表，每个学生评分用整数表示。

        返回值:
        int: 需要分配的糖果总数。
        """
        n = len(ratings)  # 学生数量
        candy = [1] * n  # 初始化每个学生分配的糖果数量为1

        # 从左往右遍历，保证右边评分更高的学生分配到更多糖果
        for i in range(n):
            if i > 0 and ratings[i-1] < ratings[i]:
                candy[i] = candy[i-1] + 1

        # 从右往左遍历，保证左边评分更高的学生分配到更多糖果
        for i in range(n-1, -1, -1):
            if i < n-1 and ratings[i] > ratings[i+1]:
                if candy[i] < candy[i+1] + 1:
                    candy[i] = candy[i+1] + 1

        return sum(candy)  # 返回糖果总数
# @lc code=end
s = Solution()
print(s.candy([1,2,2]))
print(s.candy([1,3,2,2,1]))
