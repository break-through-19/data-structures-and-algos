"""
Selection Sort Algorithm

Time complexity
Best - Ω(n^2)
Average - θ(n^2)
Worst - O(n^2)

Space Complexity - O(1)
"""

class Solution:

    def selectionSort(self, arr, n):
        # code here
        for curr_idx in range(0, n):
            min_idx = curr_idx

            # Selects min_idx in given range
            for range_iterator in range(curr_idx+1, n):
                min_idx = range_iterator if arr[range_iterator] < arr[min_idx] else min_idx

            # Swaps if curr_idx doesn't have min element
            if min_idx != curr_idx:
                # Swapping without using temp variable
                arr[curr_idx] = arr[curr_idx] + arr[min_idx]
                arr[min_idx] = arr[curr_idx] - arr[min_idx]
                arr[curr_idx] = arr[curr_idx] - arr[min_idx]