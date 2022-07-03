"""
https://www.programiz.com/dsa/priority-queue
Operations
1. Insert
2. Delete
3. Modify priority by a Key
4. Peek
5. Pop
6. Heapify

Utils
1. Sift Up by index
2. Sift Down by index
3. Get Parent
4. Get Left Child
5. Get Right Child

Structure
key, priority

"""
import sys
from typing import List



class PriorityQueueItem:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority


class MinPriorityQueue:
    # ------------------------HEAP OPERATIONS-------------------------------
    @classmethod
    def heapify(cls, list: List[PriorityQueueItem]):
        listSize = len(list)

        for pos in reversed(range(listSize // 2)):  # Todo: Dont forget
            cls._siftDownByIndex(list, pos)

    @classmethod
    def heapPush(cls, minHeap: List[PriorityQueueItem], data: PriorityQueueItem):
        minHeap.append(data)
        cls._siftUpByIndex(minHeap, len(minHeap) - 1)

    @classmethod
    def heapPop(cls, minHeap: List[PriorityQueueItem]) -> int:
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
    def heapPeek(cls, minHeap: List[PriorityQueueItem]) -> int:
        if len(minHeap) > 0:
            return minHeap[0]
        else:
            raise IndexError("Heap is empty. Please add at least one element and retry the operation")

    @classmethod
    def modifyPriority(cls, minHeap, key, newPriority):
        oldPriority = sys.maxsize
        pos = 0
        heapSize = len(minHeap)
        while pos < heapSize:
            if minHeap[pos].key == key:
                oldPriority = minHeap[pos].priority
                minHeap[pos].priority = newPriority
                break
            pos += 1

        if newPriority < oldPriority:
            cls._siftUpByIndex(minHeap, pos)
        else:
            cls._siftDownByIndex(minHeap, pos)



    # ------------------------HEAP UTIL FUNCTIONS-------------------------------
    @classmethod
    def _siftDownByIndex(cls, minHeap: List[PriorityQueueItem], startIndex: int):

        while cls._hasLeftChild(minHeap, startIndex):  # Todo: Dont forget
            minIndex = cls._getLeftChild(startIndex)

            if cls._hasRightChild(minHeap, startIndex) and minHeap[cls._getRightChild(startIndex)].priority < minHeap[minIndex].priority:
                minIndex = cls._getRightChild(startIndex)

            # Check if heap had reached the correct state
            if minHeap[startIndex].priority < minHeap[minIndex].priority:
                break
            else:
                minHeap[startIndex], minHeap[minIndex] = minHeap[minIndex], minHeap[startIndex]
                startIndex = minIndex

    @classmethod
    def _siftUpByIndex(cls, minHeap: List[PriorityQueueItem], startIndex: int):

        while cls._hasParent(startIndex) and minHeap[cls._getParent(startIndex)].priority > minHeap[startIndex].priority:
            parentIndex = cls._getParent(startIndex)
            minHeap[startIndex], minHeap[parentIndex] = minHeap[parentIndex], minHeap[startIndex]
            startIndex = parentIndex

    @classmethod
    def _hasParent(cls, index: int):
        return cls._getParent(index) >= 0

    @classmethod
    def _getParent(cls, childIndex: int):
        return (childIndex - 1) // 2  # Todo: Dont forget

    @classmethod
    def _hasLeftChild(cls, minHeap: List[PriorityQueueItem], index: int):
        return cls._getLeftChild(index) < len(minHeap)

    @classmethod
    def _hasRightChild(cls, minHeap: List[PriorityQueueItem], index: int):
        return cls._getRightChild(index) < len(minHeap)

    @classmethod
    def _getLeftChild(cls, index: int):
        return index * 2 + 1

    @classmethod
    def _getRightChild(cls, index: int):
        return index * 2 + 2


minHeap1 = []
# MinPriorityQueue.heapPop(minHeap1)
MinPriorityQueue.heapPush(minHeap1, PriorityQueueItem("Alice", 4))
for heapItem in minHeap1: print(vars(heapItem))
print()
MinPriorityQueue.heapPush(minHeap1, PriorityQueueItem("Bob", 3))
for heapItem in minHeap1: print(vars(heapItem))
print()

MinPriorityQueue.heapPush(minHeap1, PriorityQueueItem("Cat", 2))
for heapItem in minHeap1: print(vars(heapItem))
print()

MinPriorityQueue.heapPush(minHeap1, PriorityQueueItem("Dog", 1))
for heapItem in minHeap1: print(vars(heapItem))
print()

MinPriorityQueue.modifyPriority(minHeap1, "Dog", 100)
print("After modifying Dog's priority from 1 --> 100")
for heapItem in minHeap1: print(vars(heapItem))
print()

MinPriorityQueue.modifyPriority(minHeap1, "Cat", 200)
print("After modifying Cat's priority from 2 --> 200")
for heapItem in minHeap1: print(vars(heapItem))
print()

MinPriorityQueue.modifyPriority(minHeap1, "Cat", 1)
print("After modifying Cat's priority from 200 --> 1")
for heapItem in minHeap1: print(vars(heapItem))
print()

list = [PriorityQueueItem("Hi", 3), PriorityQueueItem("Hello", 4), PriorityQueueItem("Hey", 10)]
MinPriorityQueue.heapify(list)
for heapItem in list: print(vars(heapItem))
print()


print("Popped: ", vars(MinPriorityQueue.heapPop(list)))
print("Peeked: ", vars(MinPriorityQueue.heapPeek(list)))
for heapItem in list: print(vars(heapItem))
print()


print("Popped: ", vars(MinPriorityQueue.heapPop(list)))
print("Peeked: ", vars(MinPriorityQueue.heapPeek(list)))
for heapItem in list: print(vars(heapItem))
print()

print("Popped: ", vars(MinPriorityQueue.heapPop(list)))
# print("Peeked: ", vars(MinPriorityQueue.heapPeek(list)))


