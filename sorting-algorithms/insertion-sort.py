"""
Insertion Sort Algorithm
Time Complexity
Best - Ω(n)
Average - θ(n^2)
Worst - O(n^2)

Space complexity - O( 1 )

"""
class Solution:
    def insert(self, alist, index, n):
        # code here
        curr_ele = alist[index];
        hole_idx = index
        for iterator in reversed(range(index)):
            if (alist[iterator] > curr_ele):
                alist[hole_idx] = alist[iterator]
                hole_idx = iterator
            else:
                break

        alist[hole_idx] = curr_ele

    # Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        # code here
        # Divide array to sorted and unsorted subset
        # Let sorted array keep growing from 0 to N
        # Pick out the next element in list and insert it in appropriate position
        # by comparing with the sorted subset
        for sortedSubsetItr in range(0, n):
            self.insert(alist, sortedSubsetItr, n)
