#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# https://leetcode.cn/problems/course-schedule/description/
#
# algorithms
# Medium (53.90%)
# Likes:    1898
# Dislikes: 0
# Total Accepted:    379.5K
# Total Submissions: 703.8K
# Testcase Example:  '2\n[[1,0]]'
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi]
# ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
# 示例 2：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
# 提示：
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同
#
#
#
from typing import List, Optional
import collections
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)] # 0: 未访问, 1: 正在访问, -1: 已访问
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 标签 表示有向图 邻接矩阵 邻接表 拓扑排序 all() any()
        # 模板 拓扑排序
        """
        1. 先将所有节点入度置为0
        2. 遍历所有边, 将边的起点的入度加1
        3. 遍历所有节点, 将入度为0的节点加入队列
        4. 循环遍历队列直至队列为空, 将队列中的节点出队列, 将该节点的后继节点的入度-1
        """

        # v2.1 defaultdict -> dict, 优化了入度为0的课程列表的构建过程, deque -> list.
        indegree = [0] * numCourses  # 初始化入度数组
        adjacency = {i: [] for i, _ in enumerate(indegree)}  # 初始化邻接表

        # 填充邻接表和入度数组
        for pre in prerequisites:
            adjacency[pre[1]].append(pre[0]) # pre[1] -> pre[0]
            indegree[pre[0]] += 1

        # 构造入度为0的课程列表
        indegreeZero = [i for i in range(numCourses) if indegree[i] == 0]

        # BFS TopSort 进行拓扑排序的过程
        while indegreeZero:
            i = indegreeZero.pop()  # 当前入度为0的课程
            for j in adjacency.get(i, []):  # 获取当前课程的后继课程列表 (读完当前课程，后继课程入度-1)
                indegree[j] -= 1  # 减少后继课程的入度
                if indegree[j] == 0:  # 如果后继课程的入度也变为0，加入列表
                    indegreeZero.append(j)

        # 如果所有课程的入度都变为0，则可以完成所有课程
        return all(i == 0 for i in indegree)

        # v2 添加了一个用于维护入度为0的课程的队列, 优化了时间复杂度
        indegree = [0] * numCourses # 入度数组
        adjacency = collections.defaultdict(list) # 邻接表
        # indegreeZero = [] # 入度为0的课程队列

        for pre in prerequisites:
            adjacency[pre[1]].append(pre[0])
            indegree[pre[0]] += 1

        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         indegreeZero.append(i)

        indegreeZero = collections.deque([i for i in range(numCourses) if indegree[i] == 0])

        while indegreeZero:
            i = indegreeZero.pop()
            for j in adjacency[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    indegreeZero.append(j)

        return all(i == 0 for i in indegree)

        # v1.1 邻接矩阵 -> 基于字典的邻接表, 性能提升有限
        indegree = [0] * numCourses # 入度数组
        adjacency = collections.defaultdict(list)
        for pre in prerequisites:
            adjacency[pre[1]].append(pre[0])
            indegree[pre[0]] += 1
        def findIndegreeZero() -> int: # 找入度为0的点
            for i in range(numCourses):
                if indegree[i] == 0:
                    indegree[i] = -1 # -1: 标记为删除
                    return i
            return -1
        i = findIndegreeZero()
        while i != -1:
            for j in adjacency[i]:
                indegree[j] -= 1 # j的入度-1
            i = findIndegreeZero()
        return all(i == -1 for i in indegree)

        # v1
        indegree = [0] * numCourses # 入度数组
        adjacencyMatrix = [[0] * numCourses for _ in range(numCourses)]
        for pre in prerequisites:
            adjacencyMatrix[pre[1]][pre[0]] = 1
            indegree[pre[0]] += 1
        def findIndegreeZero() -> int: # 找入度为0的点
            for i in range(numCourses):
                if indegree[i] == 0:
                    indegree[i] = -1 # -1: 标记为删除
                    return i
            return -1
        i = findIndegreeZero()
        while i != -1:
            for j in range(numCourses):
                if adjacencyMatrix[i][j] == 1:
                    indegree[j] -= 1 # j的入度-1
                    adjacencyMatrix[i][j] = 0 # 把i->j的边去掉
            i = findIndegreeZero()
        return all(i == -1 for i in indegree)
# @lc code=end
solution = Solution()
print(solution.canFinish(2, [[1,0]]))
