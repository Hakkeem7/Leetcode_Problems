class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        # Step 1: Count frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Keep only K most frequent elements
        heap = []

        for num, count in freq.items():

            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract numbers
        return [num for count, num in heap]