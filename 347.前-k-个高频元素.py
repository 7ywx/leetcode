#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode.cn/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.60%)
# Likes:    1805
# Dislikes: 0
# Total Accepted:    528.3K
# Total Submissions: 830.5K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 1
# k 的取值范围是 [1, 数组中不相同的元素的个数]
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的
#
#
#
#
# 进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
#
#
from typing import List, Optional
import collections
import heapq
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #TODO hashtable .keys() .values() .items() 合并字典

        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        heap = []
        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key)) #TODO 学习
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))

        return [key for val, key in heap]

        res = []
        new_nums = Counter(nums)
        # 注意这里的items()返回的是一个元组，上下文的下标操作是对元组进行的，不是对字典操作的
        sorted_nums = sorted(new_nums.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_nums[i][0])
        return res

        hashtable = collections.defaultdict(int)
        res = []
        for num in nums:
            hashtable[num] += 1
        value = hashtable.values()
        counterList = heapq.nlargest(k, hashtable.values())
        for counter in counterList:
            for key, value in hashtable.items():
                if value == counter:
                    res.append(key)
                    break
            del hashtable[res[-1]]
        return res
# @lc code=end
s = Solution()
s.topKFrequent([1,1,1,2,2,3], 2)
s.topKFrequent([-1,-1], 1)
