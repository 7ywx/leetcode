#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode.cn/problems/search-insert-position/description/
#
# algorithms
# Easy (46.00%)
# Likes:    2279
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3M
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
#
# 示例 3:
#
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 为 无重复元素 的 升序 排列数组
# -10^4 <= target <= 10^4
#
#
#
from typing import List
# @lc code=sta
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        left, right = 0, nums_length-1
        if target < nums[left]:
            return 0
        if nums[right] < target:
            return nums_length
        while left != right - 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return right
# @lc code=end
s = Solution()
# print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3],1))
