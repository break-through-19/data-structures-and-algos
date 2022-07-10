"""
Heap Sort Algorithm

Time complexity - O ( N logN )
Space complexity - O( 1 )

"""


class Solution:
    def HeapSort(self, array, arrLen):
        # Build Max Heap - using Heapify
        for itr in range((arrLen // 2) - 1, -1, -1): # Internal node starts from (arrLen // 2) - 1 index
            self.siftDownByIndex_recursive(array, arrLen, itr)

        # Pick max and created sorted array in place
        for itr in range(arrLen - 1, -1, -1):
            self.swapArrayElements(array, 0, itr)
            self.siftDownByIndex_recursive(array, itr, 0)

    def siftDownByIndex_recursive(self, array, arrLen, position):
        leftChildPos = 2 * position + 1
        rightChildPos = leftChildPos + 1
        maxElePos = position

        if leftChildPos < arrLen and array[leftChildPos] > array[maxElePos]:
            maxElePos = leftChildPos
        if rightChildPos < arrLen and array[rightChildPos] > array[maxElePos]:
            maxElePos = rightChildPos

        if position != maxElePos:
            self.swapArrayElements(array, position, maxElePos)
            self.siftDownByIndex_recursive(array, arrLen, maxElePos)

    def swapArrayElements(self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp

