#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
# https://leetcode.cn/problems/evaluate-division/description/
#
# algorithms
# Medium (58.73%)
# Likes:    1126
# Dislikes: 0
# Total Accepted:    107.6K
# Total Submissions: 183.2K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和
# values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
#
# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj =
# ? 的结果作为答案。
#
# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0
# 替代这个答案。
#
# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
#
# 注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。
#
#
#
# 示例 1：
#
#
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
# 注意：x 是未定义的 => -1.0
#
# 示例 2：
#
#
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
#
#
# 示例 3：
#
#
# 输入：equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#
#
#
#
# 提示：
#
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj 由小写英文字母与数字组成
#
#
#

# @lc code=start

from collections import deque, defaultdict
from typing import List

class Solution:
    class Edge:
        def __init__(self, node: str, weight: float):
            self.node = node
            self.weight = weight

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 把 equations 抽象成一幅图，邻接表存储
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            w = values[i]
            # 构建双向图
            graph[a].append(self.Edge(b, w))
            graph[b].append(self.Edge(a, 1.0 / w))

        res = []
        for query in queries:
            start, end = query
            # BFS 遍历图，计算 start 到 end 的路径乘积
            res.append(self.bfs(graph, start, end))
        return res

    def bfs(self, graph: defaultdict, start: str, end: str) -> float:
        if start not in graph or end not in graph:
            # 不存在的节点，肯定无法到达
            return -1.0
        if start == end:
            return 1.0

        # BFS 标准框架
        queue = deque([start])
        visited = set([start])

        # key 为节点 ID（变量名），value 记录从 start 到该节点的路径乘积
        weight = {start: 1.0}

        while queue:
            cur = queue.popleft()
            for neighbor in graph[cur]:
                if neighbor.node in visited:
                    continue
                # 更新路径乘积
                weight[neighbor.node] = weight[cur] * neighbor.weight
                if neighbor.node == end:
                    return weight[end]
                # 记录 visited
                visited.add(neighbor.node)
                # 新节点加入队列继续遍历
                queue.append(neighbor.node)
        return -1.0
# @lc code=end
