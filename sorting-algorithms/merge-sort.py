"""
Merge Sort Algorithm
Time Complexity
Best - Ω(n log n)
Average - θ(n log n)
Worst - O(n log n)

Space complexity - O( n )
"""

class Solution:
    def merge(self, nums, left, mid, right):
        # Merge two sorted halves nums[left:mid] and nums[mid:right+1] into nums
        left_half = nums[left:mid]
        right_half = nums[mid:right + 1]

        left_idx = right_idx = 0
        curr_idx = left

        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] <= right_half[right_idx]:
                nums[curr_idx] = left_half[left_idx]
                left_idx += 1
            else:
                nums[curr_idx] = right_half[right_idx]
                right_idx += 1
            curr_idx += 1

        while left_idx < len(left_half):
            nums[curr_idx] = left_half[left_idx]
            left_idx += 1
            curr_idx += 1

        while right_idx < len(right_half):
            nums[curr_idx] = right_half[right_idx]
            right_idx += 1
            curr_idx += 1

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

