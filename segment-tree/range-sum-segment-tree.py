"""

https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/

Most useful Tree based DS for Range based queries

Pre-requisite
Build -> Time complexity = O(N)
For N node 2N - 1 nodes will be present in Segment Tree

Space Complexity - O(N)

Operations
1. Query for a given range - O( log N )
2. Update for a given leaf node - O( log N )
"""


class RangeSumSegmentTree:

    # Space complexity - O(N)
    def __init__(self, numericList):
        self.actualList = numericList
        self.sumSegmentTree = [0] * (2 * len(numericList) - 1)
        self._build_segment_tree(0, len(self.actualList) - 1)

    # Time complexity O(2*N) --> O(N)
    def _build_segment_tree(self, list_left, list_right, node_position = 0):

        if list_left == list_right:
            self.sumSegmentTree[node_position] = self.actualList[list_left]

        else:
            mid = (list_left + list_right) // 2
            left_child_pos = 2 * node_position + 1
            right_child_pos = 2 * node_position + 2
            self._build_segment_tree(list_left, mid, left_child_pos)
            self._build_segment_tree(mid + 1, list_right, right_child_pos)

            self.sumSegmentTree[node_position] = self.sumSegmentTree[left_child_pos] + self.sumSegmentTree[right_child_pos]

    # Time complexity O(log N)
    def update_segment_tree(self, list_position, new_value):
        def _update_segment_tree(list_left, list_right, node_position = 0):
            if list_left == list_right and list_right == list_position:
                self.actualList[list_position] = new_value
                self.sumSegmentTree[node_position] = new_value

            else:
                mid = (list_left + list_right) // 2
                left_child_pos = 2 * node_position + 1
                right_child_pos = 2 * node_position + 2

                if list_position <= mid:
                    _update_segment_tree(list_left, mid, left_child_pos)
                else:
                    _update_segment_tree(mid + 1, list_right, right_child_pos)

                self.sumSegmentTree[node_position] = self.sumSegmentTree[left_child_pos] + self.sumSegmentTree[right_child_pos]

        _update_segment_tree(0, len(self.actualList) - 1)

    # Time complexity O(log N)
    def query_range(self, start_interval, end_interval) -> int:
        def _query_range(left, right, node_position = 0):
            # Querying interval is completely WITHIN the segment tree node interval
            if start_interval <= left <= right <= end_interval:
                return self.sumSegmentTree[node_position]

            # Querying interval is completely OUTSIDE the segment tree node interval
            if end_interval < left or start_interval > right:
                return 0

            mid = (left + right) // 2
            left_child_val = _query_range(left, mid, 2*node_position+1)
            right_child_val = _query_range(mid+1, right, 2*node_position+2)

            return left_child_val + right_child_val

        return _query_range(0, len(self.actualList)-1)


ascendingList = [i for i in range(1, 10)]
sumSegmentTree1 = RangeSumSegmentTree(ascendingList)

print(sumSegmentTree1.actualList)
print(sumSegmentTree1.sumSegmentTree)

sumSegmentTree1.update_segment_tree(8, 100)

print(sumSegmentTree1.actualList)
print(sumSegmentTree1.sumSegmentTree)

print(sumSegmentTree1.query_range(0, len(ascendingList)-1))
print(sumSegmentTree1.query_range(0, len(ascendingList)-2))
print(sumSegmentTree1.query_range(7, len(ascendingList)-1))
