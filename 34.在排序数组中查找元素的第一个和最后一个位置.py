#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (43.21%)
# Likes:    2649
# Dislikes: 0
# Total Accepted:    949.1K
# Total Submissions: 2.2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0:
            return [-1, -1]
        left = 0
        right = nums_len - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else: # nums[mid] == target
                left, right = mid, mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < nums_len - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
        return [-1, -1]
# @lc code=end
s = Solution()
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
