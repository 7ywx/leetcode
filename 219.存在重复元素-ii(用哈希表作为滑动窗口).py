#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode.cn/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (47.51%)
# Likes:    724
# Dislikes: 0
# Total Accepted:    329.5K
# Total Submissions: 693.4K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i
# - j) <= k 。如果存在，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
#
# 示例 2：
#
#
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
#
# 示例 3：
#
#
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
#
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 0 <= k <= 10^5
#
#
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 滑动窗口
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False

        # 哈希表
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False
# @lc code=end
