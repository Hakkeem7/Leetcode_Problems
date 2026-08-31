class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        i = 0

        while i < n:

            correctIndex = nums[i] - 1

            if (
                1 <= nums[i] <= n
                and nums[i] != nums[correctIndex]
            ):
                nums[i], nums[correctIndex] = (
                    nums[correctIndex],
                    nums[i]
                )

            else:
                i += 1

        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1
        