#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode.cn/problems/container-with-most-water/description/
#
# algorithms
# Medium (60.01%)
# Likes:    4794
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.9M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例 1：
#
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例 2：
#
#
# 输入：height = [1,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         if min(height[i], height[j]) * (j - i) > maxArea:
        #             maxArea = min(height[i], height[j]) * (j - i)
        # # print(maxArea)
        # return maxArea
        # i, j = 0, len(height) - 1
        # while i < j:
        #     maxArea = max(maxArea, min(height[i], height[j]) * (j - i))
        #     if height[i] < height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # # print(maxArea)
        # return maxArea
        left, right, maxArea = 0, len(height) - 1, 0
        maxh = max(height)
        while left < right:
            if height[left] < height[right]:
                maxArea = max(maxArea, height[left] * (right - left))
                left += 1
            else:
                maxArea = max(maxArea, height[right] * (right - left))
                right -= 1
            if maxArea >= maxh * (right - left): # 即使后续的高度再大（再大也不能大过maxh），容器的宽度已经变小，面积不可能再大于已经得到的最大面积。
                break
        return maxArea
# @lc code=end
solution = Solution()
solution.maxArea([1,8,6,2,5,4,8,3,7])
