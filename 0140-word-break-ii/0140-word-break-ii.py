class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert list to set for faster lookup
        word_set = set(wordDict)

        # Memoization dictionary
        memo = {}

        return self.backtrack(s, 0, word_set, memo)

    def backtrack(self, s, start, word_set, memo):

        # Base case: reached the end of the string
        if start == len(s):
            return [""]

        # Already calculated
        if start in memo:
            return memo[start]

        result = []

        # Try every possible word starting from 'start'
        for end in range(start + 1, len(s) + 1):

            word = s[start:end]

            # If word exists in dictionary
            if word in word_set:

                remaining = self.backtrack(
                    s, end, word_set, memo
                )

                for sentence in remaining:

                    if sentence == "":
                        result.append(word)
                    else:
                        result.append(word + " " + sentence)

        # Store result for this starting index
        memo[start] = result

        return result