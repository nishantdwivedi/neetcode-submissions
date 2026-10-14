import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        heap = []

        # Keep only the K most frequent elements
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif count > heap[0][0]:
                heapq.heapreplace(heap, (count, num))

        return [num for count, num in heap]