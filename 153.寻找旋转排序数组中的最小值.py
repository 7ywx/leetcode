#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (57.42%)
# Likes:    1087
# Dislikes: 0
# Total Accepted:    447.8K
# Total Submissions: 779.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7]
# 在变化后可能得到：
#
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
#
#
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 3 次得到输入数组。
#
#
# 示例 3：
#
#
# 输入：nums = [11,13,15,17]
# 输出：11
# 解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums 中的所有整数 互不相同
# nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right: # 区间不为空
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid # mid可能是旋转点, 如果用mid-1, 有可能错过
            else:
                left = mid + 1
        return nums[left]
# @lc code=end
def printStation(nums, l, r):
    nums_len = len(nums)
    for i in range(nums_len):
        if i == l:
            print("l", end=" ")
        elif i == r:
            print("r", end="")
        else:
            print(" ", end=" ")
    print()
    for num in nums: print(num, end=" ")
    print()

s = Solution()
# s.findMin([3,4,5,1,2])
s.findMin([5,6,7,1,2,3,4])
