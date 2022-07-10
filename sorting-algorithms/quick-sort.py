"""
Quick Sort Algorithm
Time Complexity
Best - Ω(n log n)
Average - θ(n log n)
Worst - O(n^2)

Space complexity - O( 1 )
"""


class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            partitionIdx = self.partition(arr, low, high)
            self.quickSort(arr, low, partitionIdx - 1)
            self.quickSort(arr, partitionIdx + 1, high)

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