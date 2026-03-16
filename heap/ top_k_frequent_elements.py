import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for n in nums:
            frequency[n] = frequency.get(n,0) + 1

        heap = []

        for num, freq in frequency.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap] 