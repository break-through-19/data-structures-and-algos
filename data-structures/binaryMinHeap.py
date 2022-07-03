"""
https://www.programiz.com/dsa/heap-data-structure
Operations
1. Insert
2. Delete top / Extract min
4. Peek
5. Pop
6. Heapify

Utils
1. Sift Up by index / Heapify Up
2. Sift Down by index / Heapify Down
3. Get Parent
4. Get Left Child
5. Get Right Child

"""

from typing import List

class MinHeap:
    #------------------------HEAP OPERATIONS-------------------------------
    @classmethod
    def heapify(cls, list: List[int]):
        listSize = len(list)

        for pos in reversed(range(listSize // 2)): #Todo: Dont forget
            cls._siftDownByIndex(list, pos)

    @classmethod
    def heapPush(cls, minHeap: List[int], data: int):
        minHeap.append(data)
        cls._siftUpByIndex(minHeap, len(minHeap)-1)

    @classmethod
    def heapPop(cls, minHeap: List[int]) -> int:
        heapSize = len(minHeap)
        if heapSize == 0:
            raise IndexError("Heap is empty. Please add at least one element and retry the operation")
        else:
            poppedElement = minHeap[0]
            if len(minHeap) > 1:
                minHeap[0] = minHeap.pop()
                cls._siftDownByIndex(minHeap, 0)
            else:
                minHeap.pop(0)
            return poppedElement

    @classmethod
    def heapPeek(cls, minHeap: List[int]) -> int:
        if len(minHeap) > 0:
            return minHeap[0]
        else:
            raise IndexError("Heap is empty. Please add at least one element and retry the operation")

    #------------------------HEAP UTIL FUNCTIONS-------------------------------
    @classmethod
    def _siftDownByIndex(cls, minHeap, startIndex):

        while cls._hasLeftChild(minHeap, startIndex): #Todo: Dont forget
            minIndex = cls._getLeftChild(startIndex)

            if cls._hasRightChild(minHeap, startIndex) and minHeap[cls._getRightChild(startIndex)] < minHeap[minIndex]:
                minIndex = cls._getRightChild(startIndex)

            # Check if heap had reached the correct state
            if minHeap[startIndex] < minHeap[minIndex]:
                break
            else:
                minHeap[startIndex], minHeap[minIndex] = minHeap[minIndex], minHeap[startIndex]
                startIndex = minIndex

    @classmethod
    def _siftUpByIndex(cls, minHeap, startIndex):

        while cls._hasParent(startIndex) and minHeap[cls._getParent(startIndex)] > minHeap[startIndex]:
            parentIndex = cls._getParent(startIndex)
            minHeap[startIndex], minHeap[parentIndex] = minHeap[parentIndex], minHeap[startIndex]
            startIndex = parentIndex

    @classmethod
    def _hasParent(cls, index):
        return cls._getParent(index) >= 0

    @classmethod
    def _getParent(cls, childIndex):
        return (childIndex - 1) // 2 #Todo: Dont forget

    @classmethod
    def _hasLeftChild(cls, minHeap, index):
        return cls._getLeftChild(index) < len(minHeap)

    @classmethod
    def _hasRightChild(cls, minHeap, index):
        return cls._getRightChild(index) < len(minHeap)

    @classmethod
    def _getLeftChild(cls, index):
        return index*2 + 1

    @classmethod
    def _getRightChild(cls, index):
        return index*2 + 2


minHeap1 = []
# MinHeap.heapPop(minHeap1)
MinHeap.heapPush(minHeap1, 4)
print(minHeap1)
MinHeap.heapPush(minHeap1, 3)
print(minHeap1)
MinHeap.heapPush(minHeap1, 2)
print(minHeap1)
MinHeap.heapPush(minHeap1, 1)
print(minHeap1)

list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
MinHeap.heapify(list)
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)

print("Popped: ", MinHeap.heapPop(list))
print("Peeked: ", MinHeap.heapPeek(list))
print(list)
