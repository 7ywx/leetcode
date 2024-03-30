#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode.cn/problems/jump-game/description/
#
# algorithms
# Medium (43.29%)
# Likes:    2702
# Dislikes: 0
# Total Accepted:    915.6K
# Total Submissions: 2.1M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        判断一个数组中的元素是否能够让人从数组的开始位置跳到结束位置。

        参数:
        nums: 一个整数数组，表示每个位置上的最大跳跃步数。

        返回值:
        返回一个布尔值，True表示可以跳跃到数组的结束位置，False表示不能。
        """
        jump = 0  # 当前能够跳跃的最远位置

        for i in range(len(nums)):
            # 如果当前位置已经超过当前能跳的最远位置，表示无法继续跳跃到数组末尾
            if jump < i:
                return False

            # 更新当前能够跳跃的最远位置
            if i + nums[i] > jump:
                jump = i + nums[i]

        return True

        # n = len(nums)
        # farthest = 0
        # for i in range(n - 1):
        #     # 不断计算能跳到的最远距离
        #     farthest = max(farthest, i + nums[i])
        #     # 可能碰到了 0，卡住跳不动了
        #     if farthest <= i:
        #         return False
        # return farthest >= n - 1

# @lc code=end
