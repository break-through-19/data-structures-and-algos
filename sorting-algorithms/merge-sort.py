"""
Merge Sort Algorithm
Time Complexity
Best - Ω(n log n)
Average - θ(n log n)
Worst - O(n log n)

Space complexity - O( n )
"""

import math

class Solution:
    def merge(self, arr, l, mid, r):
        # code here
        leftArr = []
        rightArr = []
        leftLen = mid - l
        rightLen = r + 1 - mid
        for leftItr in range(l, mid):
            leftArr.append(arr[leftItr])

        for rightItr in range(mid, r + 1):
            rightArr.append(arr[rightItr])

        currArrItr = l
        leftItr = 0
        rightItr = 0

        while leftItr < leftLen and rightItr < rightLen:
            if leftArr[leftItr] < rightArr[rightItr]:
                arr[currArrItr] = leftArr[leftItr]
                leftItr += 1
            else:
                arr[currArrItr] = rightArr[rightItr]
                rightItr += 1
            currArrItr += 1

        while leftItr < leftLen:
            arr[currArrItr] = leftArr[leftItr]
            leftItr += 1
            currArrItr += 1

        while rightItr < rightLen:
            arr[currArrItr] = rightArr[rightItr]
            rightItr += 1
            currArrItr += 1

    def mergeSort(self, arr, l, r):
        # code here
        # Todo - Remember arrLen calc
        arrLen = (r+1 - l)

        # Base condition
        if arrLen < 2:
            return

        # Todo - Remember mid calc
        mid = (l + r+1) // 2
        self.mergeSort(arr, l, mid - 1)
        self.mergeSort(arr, mid, r)

        self.merge(arr, l, mid, r)

