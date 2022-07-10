"""
Optimized - Quick Sort Algorithm
Time Complexity
Best - Ω(n log n)
Average - θ(n log n)
Worst - O(n log n)

Space complexity - O( 1 )
"""

from random import randint


class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            partitionIdx = self.randomPartition(arr, low, high)
            # The element in partionIdx is in its correct place
            # So sort the set of elements before and after that
            self.quickSort(arr, low, partitionIdx - 1)
            self.quickSort(arr, partitionIdx + 1, high)

    # Important logic
    def partition(self, arr, low, high):
        # Element for which we will find the right Partition Index
        partitionEle = arr[high]

        # Initialized to low for now
        partitionIdx = low

        for leftPtr in range(low, high):
            # Less than or Equal (<=) is used as the elements to left of partition index is not strictly sorted
            if arr[leftPtr] <= partitionEle:
                arr[partitionIdx], arr[leftPtr] = arr[leftPtr], arr[partitionIdx]
                partitionIdx += 1

        arr[partitionIdx], arr[high] = arr[high], arr[partitionIdx]
        return partitionIdx

    def randomPartition(self, arr, low, high):
        # Important step
        randomIdx = randint(low, high)
        arr[randomIdx], arr[high] = arr[high], arr[randomIdx]
        return self.partition(arr, low, high)

