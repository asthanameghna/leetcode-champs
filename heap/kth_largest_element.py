# # 215. Kth Largest Element in an Array

# ## Approach

# Use a **min heap of size `k`** to keep track of the `k` largest elements seen so far.

# 1. Initialize an empty min heap.
# 2. Iterate through each number in `nums`.
# 3. Push the number into the heap.
# 4. If the heap size becomes greater than `k`, remove the smallest element from the heap.
# 5. After processing all numbers, the heap will contain the `k` largest elements.
# 6. The smallest element in the heap (`heap[0]`) is the **kth largest element**.

# The heap ensures we only keep the `k` largest elements at any time.

# ---

# ## Time Complexity

# **O(n log k)**

# - We iterate through `n` elements.
# - Each push/pop operation on the heap costs `O(log k)`.
# - The heap never grows larger than `k`.

# ---

# ## Space Complexity

# **O(k)**

# - The heap stores at most `k` elements.


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]        
        