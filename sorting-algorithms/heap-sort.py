"""
Heap Sort Algorithm

Time complexity - O ( N logN )
Space complexity - O( 1 )

"""


class Solution:
    def HeapSort(self, array, arrLen):
        # Build Max Heap - using Heapify
        # Time Complexity: O(n) amortized - bottom-up heap construction
        # Loop runs ~n/2 times, but most nodes are near bottom (don't sift far)
        for itr in range((arrLen // 2) - 1, -1, -1): # Internal node starts from (arrLen // 2) - 1 index
            self.siftDownByIndex_recursive(array, arrLen, itr)  # O(log n) worst case per call, but O(n) overall

        # Pick max and created sorted array in place
        # Time Complexity: O(n log n) - extract max n times, each takes O(log n)
        for itr in range(arrLen - 1, -1, -1):
            self.swapArrayElements(array, 0, itr)  # O(1)
            self.siftDownByIndex_recursive(array, itr, 0)  # O(log n) - sift down from root

    def siftDownByIndex_recursive(self, array, arrLen, position):
        leftChildPos = 2 * position + 1
        rightChildPos = leftChildPos + 1
        maxElePos = position

        if leftChildPos < arrLen and array[leftChildPos] > array[maxElePos]:
            maxElePos = leftChildPos
        if rightChildPos < arrLen and array[rightChildPos] > array[maxElePos]:
            maxElePos = rightChildPos

        # Swap and recurse if needed - O(log n) worst case (recursive depth)
        if position != maxElePos:
            self.swapArrayElements(array, position, maxElePos)  # O(1)
            self.siftDownByIndex_recursive(array, arrLen, maxElePos)  # O(log n) - recurses down heap height

    def swapArrayElements(self, array, index1, index2):
        # Time Complexity: O(1) - constant time swap operation
        array[index1], array[index2] = array[index2], array[index1]
