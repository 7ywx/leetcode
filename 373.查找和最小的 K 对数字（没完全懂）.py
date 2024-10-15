from typing import List
#
# @lc app=leetcode.cn id=373 lang=python3
# @lcpr version=20001
#
# [373] 查找和最小的 K 对数字
#
# https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (41.43%)
# Likes:    615
# Dislikes: 0
# Total Accepted:    88.3K
# Total Submissions: 213K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
#
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
#
#
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
#
#
# 提示:
#
#
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 和 nums2 均为 升序排列
# 1 <= k <= 10^4
# k <= nums1.length * nums2.length
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 建立小根堆，push规则：先push入0,0,以后每次弹出堆顶i,j时，同时放入i+1,j和i,j+1
        # 因为i,j为当前最小的，下一个最小的要么是在剩下的堆中，不然就是i+1,j或i,j+1之一
        ans = []
        h = [(nums1[0] + nums2[0], 0, 0)]
        while len(ans) < k:
            _, i, j = heappop(h)
            ans.append([nums1[i], nums2[j]])
            # 当前最小的是i,j，放入下个元素i,j+1，但不放入i+1,j，因为如果都放入这会导致后面这两种情况出堆时，都会吧i+1,j+1入堆，导致重复
            # 但是i,0的情况下必须放入，否则每次入堆的只有0,0|0,1|0,2...
            if j == 0 and i + 1 < len(nums1):
                heappush(h, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < len(nums2):
                heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#
