#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# https://leetcode.cn/problems/maximum-subarray/description/
#
# algorithms
# Medium (55.16%)
# Likes:    6532
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2.9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max = global_max = nums[0]

        for num in nums[1:]:
            # 更新当前子数组的最大和
            current_max = max(num, current_max + num)
            # 更新全局最大子数组和
            global_max = max(global_max, current_max)
        return global_max

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i-1] + nums[i]
        return max(nums)

        # 动态规划
        dp = [0] * len(nums) # dp[i] 表示以 nums[i] 结尾的连续子数组的最大和。
        for i, num in enumerate(nums):
            if i == 0:
                dp[i] = num
            else:
                dp[i] = max(dp[i-1] + num, num) # 当前元素要么独立构成一个最大子数组（即只有它自己），要么与前面某个子数组连接形成一个新的最大子数组。
        return max(dp)
# @lc code=end
solution = Solution()
solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
solution.maxSubArray([5,4,-1,7,8])
