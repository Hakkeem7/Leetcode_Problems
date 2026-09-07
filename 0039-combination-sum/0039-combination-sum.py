class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, total, path):

            if total == target:
                result.append(path.copy())
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                path.append(candidates[i])

                backtrack(
                    i,
                    total + candidates[i],
                    path
                )

                path.pop()

        backtrack(0, 0, [])

        return result