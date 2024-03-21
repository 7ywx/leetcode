#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode.cn/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (64.07%)
# Likes:    2367
# Dislikes: 0
# Total Accepted:    371.7K
# Total Submissions: 579.8K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
# 示例 3 :
#
#
# 输入：nums = [3,3,3,3,3]
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
# 进阶：
#
#
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
#
#
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #TODO 快慢指针找环入口
        fast = slow = 0  # 初始化快慢指针
        # 使用快慢指针寻找环的入口
        while True: # nums[fast] and nums[nums[fast]] in range(len(nums))
            slow = nums[slow]  # 慢指针每次移动一步
            fast = nums[nums[fast]]  # 快指针每次移动两步
            if slow == fast:  # 当快慢指针相遇时
                slow = 0  # 重置慢指针到起始点
                # 使用慢快指针寻找环的起始点
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow  # 返回环的起始点

        # hashtable = {}
        # for i in nums:
        #     if i in hashtable:
        #         return i
        #     else:
        #         hashtable[i] = 1
# @lc code=end
s = Solution()
print(s.findDuplicate([2,5,9,6,9,3,8,9,7,1]))
