#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode.cn/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (45.57%)
# Likes:    2695
# Dislikes: 0
# Total Accepted:    402.2K
# Total Submissions: 882.4K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
# 示例 1:
#
#
#
#
# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
#
#
# 示例 2：
#
#
#
#
# 输入： heights = [2,4]
# 输出： 4
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #标签 单调栈
        """
        首先，要想找到第 i 位置最大面积是什么？

        是以 i 为中心，向左找第一个小于 heights[i] 的位置 left_i；
        向右找第一个小于于 heights[i] 的位置 right_i，
        即最大面积为 heights[i] * (right_i - left_i -1)
        """
        stack = [-1]  # 初始化栈，开始时放入一个哨兵值-1，便于处理边界情况
        max_area = 0  # 用于记录最大面积
        heights.append(0)  # 在末尾添加高度为0的柱子，以便能够处理数组中最后一个柱子

        for i, height in enumerate(heights):
            # 如果当前柱子的高度小于栈顶柱子的高度，说明找到了右边界
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]  # 弹出栈顶元素，并取得其高度
                w = i - stack[-1] - 1  # 计算宽度
                max_area = max(max_area, h * w)  # 更新最大面积
            stack.append(i)  # 当前柱子的索引入栈

        return max_area

        # stack = []
        # heights = [0] + heights + [0]
        # res = 0
        # for i in range(len(heights)):
        #     for s in stack:
        #         print(heights[s], end=" ")
        #     print()
        #     while stack and heights[stack[-1]] > heights[i]:
        #         tmp = stack.pop()
        #         res = max(res, (i - stack[-1] - 1) * heights[tmp])
        #     stack.append(i)
        # return res

        # n = len(heights)
        # left_i = [0] * n # 存储每个位置左边第一个小于它的位置
        # right_i = [0] * n # 存储每个位置右边第一个小于它的位置
        # left_i[0] = -1
        # right_i[-1] = n
        # for i in range(1, n):
        #     tmp = i - 1
        #     while tmp >= 0 and heights[tmp] >= heights[i]: # 找到左边的第一个小于它的位置
        #         tmp = left_i[tmp]
        #     left_i[i] = tmp
        # for i in range(n - 2, -1, -1):
        #     tmp = i + 1
        #     while tmp < n and heights[tmp] >= heights[i]:
        #         tmp = right_i[tmp]
        #     right_i[i] = tmp
        # # print(left_i)
        # # print(right_i)
        # res = 0
        # for i in range(n):
        #     res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        # return res


        # # v2
        # maxArea = 0
        # n = len(heights)
        # stack = []
        # for i in range(n):

        #     stack.append(i)

        """
        首先，要想找到第 i 位置最大面积是什么？

        是以 i 为中心，向左找第一个小于 heights[i] 的位置 left_i；
        向右找第一个小于于 heights[i] 的位置 right_i，
        即最大面积为 heights[i] * (right_i - left_i -1)
        """
        # # v1.1 暴力解法 第 i 位置的最大面积
        # maxArea = 0
        # n = len(heights)
        # for i in range(n):
        #     left, right = i-1, i+1
        #     while left > -1 and heights[left] >= heights[i]:
        #         left -= 1
        #     while right < n and heights[right] >= heights[i]:
        #         right += 1
        #     maxArea = max(maxArea, heights[i] * (right - left - 1))
        # return maxArea

        # # v1 暴力解法 败在时间限制
        # max_area = 0
        # heights_len = len(heights)
        # for i in range(heights_len):
        #     minHight = heights[i]
        #     for j in range(i, heights_len):
        #         if heights[j] < minHight:
        #             minHight = heights[j]
        #         if max_area < minHight * (j - i + 1):
        #             max_area = minHight * (j - i + 1)
        # return max_area
# @lc code=end
s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
