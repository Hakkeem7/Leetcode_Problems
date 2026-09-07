class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:

            divisor = (left + right) // 2

            total = 0

            for num in nums:
                total += (num + divisor - 1) // divisor

            if total <= threshold:
                right = divisor
            else:
                left = divisor + 1

        return left