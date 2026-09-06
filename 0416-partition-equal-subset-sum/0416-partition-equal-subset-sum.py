class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from typing import List
        total = sum(nums)

        # Cannot split an odd sum equally
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)

        # Sum 0 is always possible
        dp[0] = True

        for num in nums:

            # Go backwards
            for current_sum in range(target, num - 1, -1):

                dp[current_sum] = (
                    dp[current_sum]
                    or dp[current_sum - num]
                )

        return dp[target]