"""
Bubble Sort Algorithm
Time Complexity
Best - Ω(n)
Average - θ(n^2)
Worst - O(n^2)

Space complexity - O( 1 )
"""

class Solution:
    # Function to sort the array using bubble sort algorithm.
    def swapWithoutTemp(self, arr, index1, index2):
        arr[index1] = arr[index1] + arr[index2]
        arr[index2] = arr[index1] - arr[index2]
        arr[index1] = arr[index1] - arr[index2]

    def bubbleSort(self, arr, n):
        # code here

        # The array is sorted starting from the last index
        # At the end of every iteration arr[N] has right value, followed by arr[N-1], arr[N-2]... 0
        for listItr in range(0, n):

            # Swap Flag is to optimize bubble sort - when the array is already sorted /
            # the below range you are iterating through is already sorted, then there wouldn't be any swaps
            # Hence you break out of the loop
            swapFlag = False


            for currItr in range(0, n - listItr - 1):
                # Keep swapping to push the max element to last possible position
                if arr[currItr] > arr[currItr + 1]:
                    self.swapWithoutTemp(arr, currItr, currItr + 1)
                    swapFlag = True

            if not swapFlag:
                break