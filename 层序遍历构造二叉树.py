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

def levelOrder(root):
    if not root:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# root1 = buildTreeFromLevelOrder([5,4,8,11,None,13,4,7,2,None,None,5,1])
# levelOrder(root1)
