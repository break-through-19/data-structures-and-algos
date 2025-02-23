''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''


class Solution:
    # TC: O(log N)
    def insertToAVL(self, root, key):
        # add key to AVL (if it is not present already)
        # return root node
        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        elif key > root.data:
            root.right = self.insertToAVL(root.right, key)

        root.height = 1 + max(self._getHeight(root.left), self._getHeight(root.right))

        heightDiff = self._getHeightDiff(root)

        if heightDiff > 1 and key < root.left.data:
            # Right rotate
            return self._rightRotate(root)

        if heightDiff < -1 and key > root.right.data:
            # Left rotate
            return self._leftRotate(root)

        if heightDiff > 1 and key > root.left.data:
            # Left Right Rotate
            root.left = self._leftRotate(root.left)
            return self._rightRotate(root)

        if heightDiff < -1 and key < root.right.data:
            # Right Left rotate
            root.right = self._rightRotate(root.right)
            return self._leftRotate(root)

        return root

    def _rightRotate(self, parent2):
        """
                        parent2
                grandParent         c4
            parent1         c3

        c1          c2
        """
        grandParent = parent2.left
        parent2.left = grandParent.right
        grandParent.right = parent2

        # Order of height calc matters
        parent2.height = 1 + max(self._getHeight(parent2.left), self._getHeight(parent2.right))
        grandParent.height = 1 + max(self._getHeight(grandParent.left), self._getHeight(grandParent.right))

        return grandParent

    def _leftRotate(self, parent1):
        """
            parent1
        c1          grandParent
                c2              parent2
                            c3          c4
        """
        grandParent = parent1.right
        parent1.right = grandParent.left

        grandParent.left = parent1

        # Order of height calc matters
        parent1.height = 1 + max(self._getHeight(parent1.left), self._getHeight(parent1.right))
        grandParent.height = 1 + max(self._getHeight(grandParent.left), self._getHeight(grandParent.right))

        return grandParent

    def _getHeightDiff(self, root):
        if not root:
            return 0
        return self._getHeight(root.left) - self._getHeight(root.right)

    def _getHeight(self, root):
        if not root:
            return 0
        return root.height


# {
#  Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1


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
        n = int(input())
        ip = [int(x) for x in input().strip().split()]

        root = None

        for i in range(n):
            root = Solution().insertToAVL(root, ip[i])

            if not isBalancedBST(root):
                break

        printInorder(root)
        print()

# } Driver Code Ends