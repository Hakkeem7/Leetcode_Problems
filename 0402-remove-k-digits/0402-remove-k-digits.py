class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:

            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1

            stack.append(c)

        # If k digits are still left to remove,
        # remove them from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"
