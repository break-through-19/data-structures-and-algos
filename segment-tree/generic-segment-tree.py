"""

https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/

Most useful Tree based DS for Range based queries

Pre-requisite
Build -> Time complexity = O(N)
For N node 2N - 1 nodes will be present in Segment Tree

Operations
1. Query for a given range
2. Update for a given leaf node
"""
from unittest import TestCase

class SegmentTree():

    def __init__(self, numericList, operation_func):
        self.actualList = numericList
        self.segmentTree = [0] * (2 * len(numericList) - 1)
        self.operation_func = operation_func

        self._build_segment_tree(0, len(self.actualList) - 1)

    # Time complexity O(2*N) --> O(N)
    def _build_segment_tree(self, list_left, list_right, node_position = 0):

        if list_left == list_right:
            self.segmentTree[node_position] = self.actualList[list_left]

        else:
            mid = (list_left + list_right) // 2
            left_child_pos = 2 * node_position + 1
            right_child_pos = 2 * node_position + 2
            self._build_segment_tree(list_left, mid, left_child_pos)
            self._build_segment_tree(mid + 1, list_right, right_child_pos)

            self.segmentTree[node_position] = self.operation_func(self.segmentTree[left_child_pos], self.segmentTree[right_child_pos])

    # Time complexity O(log N)
    def update_segment_tree(self, list_position, new_value):
        def _update_segment_tree(list_left, list_right, node_position = 0):
            if list_left == list_right and list_right == list_position:
                self.actualList[list_position] = new_value
                self.segmentTree[node_position] = new_value

            else:
                mid = (list_left + list_right) // 2
                left_child_pos = 2 * node_position + 1
                right_child_pos = 2 * node_position + 2

                if list_position <= mid:
                    _update_segment_tree(list_left, mid, left_child_pos)
                else:
                    _update_segment_tree(mid + 1, list_right, right_child_pos)

                self.segmentTree[node_position] = self.operation_func(self.segmentTree[left_child_pos], self.segmentTree[
                    right_child_pos])

        _update_segment_tree(0, len(self.actualList) - 1)
    
    # Time complexity O(log N)
    def query_range(self, start_interval, end_interval) -> int:
        def _query_range(left, right, node_position = 0):
            # Querying interval is completely WITHIN the segment tree node interval
            if start_interval <= left <= right <= end_interval:
                return self.segmentTree[node_position]

            # Querying interval is completely OUTSIDE the segment tree node interval
            if end_interval < left or start_interval > right:
                return 0

            mid = (left + right) // 2
            left_child_val = _query_range(left, mid, 2*node_position+1)
            right_child_val = _query_range(mid+1, right, 2*node_position+2)

            return self.operation_func( left_child_val, right_child_val )

        return _query_range(0, len(self.actualList)-1)

class TestSegmentTree(TestCase):
    def assertGivenInputsAreEqual(self, actual, expected):
        return self.assertEqual(actual, expected)



ascendingList = [i for i in range(1, 10)]
sum_lambda = lambda x, y: x + y
min_lambda = lambda x, y: min(x, y)
max_lambda = lambda x, y: max(x, y)

sumSegmentTree = SegmentTree(ascendingList, sum_lambda)
minSegmentTree = SegmentTree(ascendingList, min_lambda)
maxSegmentTree = SegmentTree(ascendingList, max_lambda)

print(ascendingList)
# Todo: Fix tests here
testSegmentTree = TestSegmentTree()

print(f'Sum Segment Tree: {sumSegmentTree.segmentTree}')
print(testSegmentTree.assertGivenInputsAreEqual(sumSegmentTree.segmentTree, [45, 15, 30, 6, 9, 13, 17, 3, 3, 4, 5, 6, 7, 8, 9, 1, 2]))
print(f'Min Segment Tree: {minSegmentTree.segmentTree}')
print(testSegmentTree.assertGivenInputsAreEqual(minSegmentTree.segmentTree, [1, 1, 6, 1, 4, 6, 8, 1, 3, 4, 5, 6, 7, 8, 9, 1, 2]))
print(f'Max Segment Tree: {maxSegmentTree.segmentTree}')
print(testSegmentTree.assertGivenInputsAreEqual(maxSegmentTree.segmentTree, [9, 5, 9, 3, 5, 7, 9, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]))

sumSegmentTree.update_segment_tree(8, 100)
minSegmentTree.update_segment_tree(8, 100)
maxSegmentTree.update_segment_tree(8, 100)

print(sumSegmentTree.actualList)

print('After Update of 100')
print(f'Sum Segment Tree: {sumSegmentTree.segmentTree}')
print(f'Min Segment Tree: {minSegmentTree.segmentTree}')
print(f'Max Segment Tree: {maxSegmentTree.segmentTree}')

print('Sum Range Queries')
print(f'Start: 0, End: {len(ascendingList)-1} --> {sumSegmentTree.query_range(0, len(ascendingList)-1)}')
print(f'Start: 0, End: {len(ascendingList)-2} --> {sumSegmentTree.query_range(0, len(ascendingList)-2)}')
print(f'Start: 7, End: {len(ascendingList)-1} --> {sumSegmentTree.query_range(0, len(ascendingList)-1)}')

print('Min Range Queries')
print(f'Start: 0, End: {len(ascendingList)-1} --> {minSegmentTree.query_range(0, len(ascendingList)-1)}')
print(f'Start: 0, End: {len(ascendingList)-2} --> {minSegmentTree.query_range(0, len(ascendingList)-2)}')
print(f'Start: 7, End: {len(ascendingList)-1} --> {minSegmentTree.query_range(0, len(ascendingList)-1)}')

print('Max Range Queries')
print(f'Start: 0, End: {len(ascendingList)-1} --> {maxSegmentTree.query_range(0, len(ascendingList)-1)}')
print(f'Start: 0, End: {len(ascendingList)-2} --> {maxSegmentTree.query_range(0, len(ascendingList)-2)}')
print(f'Start: 7, End: {len(ascendingList)-1} --> {maxSegmentTree.query_range(0, len(ascendingList)-1)}')
