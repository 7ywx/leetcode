#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode.cn/problems/combination-sum/description/
#
# algorithms
# Medium (72.39%)
# Likes:    2736
# Dislikes: 0
# Total Accepted:    879.8K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target
# 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#
#
#
# 示例 1：
#
#
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
#
# 示例 2：
#
#
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
#
# 示例 3：
#
#
# 输入: candidates = [2], target = 1
# 输出: []
#
#
#
#
# 提示：
#
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# candidates 的所有元素 互不相同
# 1 <= target <= 40
#
#
#
from typing import List, Optional
import collections
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        作者：liweiwei1419
        链接：https://leetcode.cn/problems/combination-sum/solutions/14697/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-2/
        来源：力扣（LeetCode）
        """
        def dfs(candidates, begin, size, path, target):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], target - candidates[index])
                # Python3 的 [1, 2] + [3] 语法生成了新的列表，一层一层传到根结点以后，直接 res.append(path) 就可以了；
                # 对于可变类型（如列表或字典），则情况较为复杂，因为它们在赋值操作时实际上是引用的复制，但在函数内部对内容进行修改仍可能影响到外部的变量。
        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, target)
        return res

        #TODO 列表的列表去重
        # unique_tuple = list(set(tuple(sorted(sublist)) for sublist in res))
        # return [list(t) for t in unique_tuple]
# @lc code=end
solution = Solution()
print(solution.combinationSum([2,3,5], 8))
