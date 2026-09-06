class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # Only one house
        if n == 1:
            return nums[0]

        # Case 1: Take from first house to second-last house
        # Last house is skipped
        case1 = self.rob_linear(nums, 0, n - 2)

        # Case 2: Take from second house to last house
        # First house is skipped
        case2 = self.rob_linear(nums, 1, n - 1)

        # Return the maximum of both cases
        return max(case1, case2)

    def rob_linear(self, nums, start, end):
        # Maximum money from two houses back
        prev2 = 0

        # Maximum money from previous house
        prev1 = 0

        for i in range(start, end + 1):

            # Option 1: Skip current house
            skip = prev1

            # Option 2: Rob current house
            take = prev2 + nums[i]

            # Choose maximum
            current = max(skip, take)

            # Update previous values
            prev2 = prev1
            prev1 = current

        return prev1