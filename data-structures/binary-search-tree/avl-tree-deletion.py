''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''


def deleteNode(root, key):
    # code here
    # return root of edited tree
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None and root.right:
            return root.right
        elif root.right is None and root.left:
            return root.left
        else:
            leftMostNodeOnRight = getLeftMostNode(root.right)
            root.data = leftMostNodeOnRight.data
            root.right = deleteNode(root.right, leftMostNodeOnRight.data)

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    heightDiff = getHeightDiff(root)

    if heightDiff > 1 and getHeightDiff(root.left) >= 0:
        return rightRotate(root)
    if heightDiff < -1 and getHeightDiff(root.right) <= 0:
        return leftRotate(root)
    if heightDiff > 1 and getHeightDiff(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if heightDiff < -1 and getHeightDiff(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root


def rightRotate(parent2):
    """
                    parent2
            grandParent     C4
        parent1         C3
    C1          C2
    """
    grandParent = parent2.left
    parent2.left = grandParent.right
    grandParent.right = parent2

    parent2.height = 1 + max(getHeight(parent2.left), getHeight(parent2.right))
    grandParent.height = 1 + max(getHeight(grandParent.left), getHeight(grandParent.right))

    return grandParent


def leftRotate(parent1):
    """
        parent1
    C1      grandParent
        C2        parent2
                C3            C4
    """
    grandParent = parent1.right
    parent1.right = grandParent.left
    grandParent.left = parent1

    parent1.height = 1 + max(getHeight(parent1.left), getHeight(parent1.right))
    grandParent.height = 1 + max(getHeight(grandParent.left), getHeight(grandParent.right))

    return grandParent


def getHeightDiff(root):
    if root is None:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def getHeight(root):
    if root is None:
        return 0
    return root.height


def getLeftMostNode(root):
    while root.left:
        root = root.left
    return root


# {
#  Driver Code Starts
# Initial Template for Python 3

from collections import deque


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1


def setHeights(n):
    if not n:
        return 0
    n.height = 1 + max(setHeights(n.left), setHeights(n.right))
    return n.height


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1

    setHeights(root)
    return root


def isBST(n, lower, upper):
    if not n:
        return True

    if n.data <= lower or n.data >= upper:
        return False

    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)


def isBalanced(n):
    if not n:
        return (0, True)

    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)

    if abs(lHeight - rHeight) > 1:
        return (0, False)

    return (1 + max(lHeight, rHeight), l and r)


def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')

    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')

    else:
        return True

    return False


def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)

        n = int(input())
        ip = [int(x) for x in input().split()]

        for i in range(n):
            root = deleteNode(root, ip[i])

            if not isBalancedBST(root):
                break

        if root is None:
            print("null")
        else:
            printInorder(root)
            print()

# } Driver Code Ends