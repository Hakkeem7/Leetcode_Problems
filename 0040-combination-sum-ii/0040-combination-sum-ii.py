class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, total, path):

            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # i + 1 = use each number only once
                backtrack(i + 1, total + candidates[i], path)

                path.pop()

        backtrack(0, 0, [])

        return result