#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode.cn/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (49.06%)
# Likes:    2673
# Dislikes: 0
# Total Accepted:    538.7K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回 滑动窗口中的最大值 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# 示例 2：
#
#
# 输入：nums = [1], k = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#
import heapq
from typing import List
from typing import Optional
from collections import deque
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        max_queue = deque() # 存储的是索引，始终保持队列左边第一个的元素是最大值

        for i, num in enumerate(nums): # i是滑动窗口的右边界
            # 删除队列中小于当前元素的元素 维持单调递减
            while max_queue and nums[max_queue[-1]] < num:
                max_queue.pop()
            print("删除队列中小于当前元素的元素:", max_queue)
            # 添加当前元素的索引到队列中
            max_queue.append(i)
            print("添加当前元素的索引到队列中", max_queue)
            # 移除不在当前窗口内的索引
            while max_queue and max_queue[0] < i - k + 1:
                max_queue.popleft()
            print("移除不在当前窗口内的索引", max_queue)
            # 将当前窗口的最大值添加到结果中
            if i > k - 2: # i >= k - 1
                result.append(nums[max_queue[0]])
            print("-----------------------------------------------")
        return result

        # nums_length = len(nums)
        # left = 0
        # right = k-1
        # max_value = 0
        # result = []
        # while right < nums_length:
        #     max_value = max(nums[left:right+1])
        #     result.append(max_value)
        #     left += 1
        #     right += 1
        # return result
# @lc code=end
solution = Solution()
solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) #length = 8
