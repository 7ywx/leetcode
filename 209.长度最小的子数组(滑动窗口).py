#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.65%)
# Likes:    2216
# Dislikes: 0
# Total Accepted:    843.2K
# Total Submissions: 1.8M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#
#
# 示例 1：
#
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#
#
# 示例 2：
#
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
#
#
# 进阶：
#
#
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
#
#
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, result, bestResult = 0, 0, 0, float('inf')
        while right < len(nums):
            result += nums[right]
            while result >= target:
                bestResult = min(bestResult, right - left + 1)
                result -= nums[left]
                left += 1
            right += 1
        return bestResult if bestResult != float('inf') else 0
# @lc code=end

#标签 滑动窗口
# 最长模版
'''
# 初始化指针和结果
left, right, result, bestResult = 0, 0, 0, 0

# 循环直到右指针到达结尾
while (右指针没有到结尾):
    # 窗口扩大，加入right对应元素，更新当前result
    result += 加入元素(right)

    # 检查当前result是否不满足要求
    while (result不满足要求):
        # 窗口缩小，移除left对应元素，left右移
        result -= 移除元素(left)
        left += 1

    # 如果当前result更优，更新最佳结果
    bestResult = max(bestResult, result)

    # 右指针右移
    right += 1

# 返回最佳结果
return bestResult
'''

# 最短模版
'''
# 初始化指针和结果
left, right, result, bestResult = 0, 0, inf, inf

# 循环直到右指针到达结尾
while (右指针没有到结尾):
    # 窗口扩大，加入right对应元素，更新当前result
    result += 加入元素(right)

    # 检查当前result是否满足要求
    while (result满足要求):
        # 如果当前result更优，更新最佳结果
        bestResult = min(bestResult, result)

        # 窗口缩小，移除left对应元素，left右移
        result -= 移除元素(left)
        left += 1

    # 右指针右移
    right += 1

# 返回最佳结果
return bestResult
'''
