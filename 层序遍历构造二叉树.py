from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTreeFromLevelOrder(levelOrder):
    if not levelOrder:
        return None

    root = TreeNode(levelOrder[0])
    queue = [root]
    i = 1

    while queue:
        node = queue.pop(0)

        if i < len(levelOrder) and levelOrder[i] is not None:
            node.left = TreeNode(levelOrder[i])
            queue.append(node.left)

        i += 1

        if i < len(levelOrder) and levelOrder[i] is not None:
            node.right = TreeNode(levelOrder[i])
            queue.append(node.right)

        i += 1

    return root

# def levelOrder(root):
#     if not root:
#         return

#     queue = [root]

#     while queue:
#         node = queue.pop(0)
#         print(node.val, end=" ")

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

# root1 = buildTreeFromLevelOrder([5,4,8,11,None,13,4,7,2,None,None,5,1])
# levelOrder(root1)

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    算法流程：
        1. 特例处理： 当根节点为空，则返回空列表 [] 。
        2. 初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] 。
        3. BFS 循环： 当队列 queue 为空时跳出。
            a. 新建一个临时列表 tmp ，用于存储当前层打印结果。
            b. 当前层打印循环： 循环次数为当前层节点数（即队列 queue 长度）。
                a. 出队： 队首元素出队，记为 node。
                b. 打印： 将 node.val 添加至 tmp 尾部。
                c. 添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue 。
            c. 将当前层结果 tmp 添加入 res 。
        4. 返回值： 返回打印结果列表 res 即可。
    """
    if not root:
        return []
    res = []
    queue = collections.deque() # double-ended queue
    queue.append(root)
    while queue:
        temp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(temp)
    print(res)
    return res

def preorder(root):
    if not root:
        return ""
    res = str(root.val) + preorder(root.left) + preorder(root.right)
    # print(res)
    return res
