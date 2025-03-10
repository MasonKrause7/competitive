class TreeNode:
    def __init__(self, val, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def buildTree(root, target):
    if root.val < target:
        root.left = TreeNode(root.val+1)
        root.middle = TreeNode(root.val+2)
        root.right = TreeNode(root.val+3)

        buildTree(root.left, target)
        buildTree(root.middle, target)
        buildTree(root.right, target)

def traverseTree(root, target):
    if root.val == target:
        return 1
    elif root.val > target:
        return 0
    else:
        left_hits = traverseTree(root.left, target)
        middle_hits = traverseTree(root.middle, target)
        right_hits = traverseTree(root.right, target)

        return left_hits + middle_hits + right_hits


n = int(input())
root = TreeNode(0)
buildTree(root, n)
print(traverseTree(root, n))
