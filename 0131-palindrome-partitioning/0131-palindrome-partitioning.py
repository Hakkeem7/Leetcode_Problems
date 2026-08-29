class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def isPalindrome(string):
            return string == string[::-1]
        def backtrack(start):
            
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):

                substring = s[start:end]

                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return result

