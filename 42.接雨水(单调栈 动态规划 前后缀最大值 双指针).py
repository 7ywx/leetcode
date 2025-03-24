#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode.cn/problems/trapping-rain-water/description/
#
# algorithms
# Hard (63.23%)
# Likes:    4977
# Dislikes: 0
# Total Accepted:    847.3K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
#
#
# 示例 2：
#
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
#
#
# 提示：
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        pre_max = 0
        post_max = 0
        while left < right:
            # pre_max = max(pre_max, height[left])
            if pre_max < height[left]:
                pre_max = height[left]
            # post_max = max(post_max, height[right])
            if post_max < height[right]:
                post_max = height[right]
            if pre_max < post_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += post_max - height[right]
                right -= 1
        return ans

        # 动态规划
        # 计算height的长度
        lens = len(height)
        # 初始化总水量（答案）为0
        ans = 0

        # 前缀最大值，并将第一个元素设为height的第一个元素
        pre_max = [0] * lens
        pre_max[0] = height[0]
        # 遍历高度列表的每一个元素，计算每个元素之前的最大值
        for i in range(1, lens):
            pre_max[i] = max(pre_max[i - 1], height[i])

        # 后缀最大值，并将最后一个元素设为height的最后一个元素
        post_max = [0] * lens
        post_max[lens - 1] = height[lens - 1]
        # 遍历高度列表的每一个元素，计算每个元素之后的最大值
        for i in range(lens - 2, -1, -1):
            post_max[i] = max(post_max[i + 1], height[i])

        # 遍历高度列表的每一个元素，计算该元素可以盛水量
        for h, p, q in zip(height, pre_max, post_max):
            ans += min(p, q) - h

        # 返回总水量（答案）
        return ans
# @lc code=end
