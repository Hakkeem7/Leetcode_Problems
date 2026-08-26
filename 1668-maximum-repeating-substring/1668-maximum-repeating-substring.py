class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k=0
        rep=""
        while (rep+word) in sequence:
            rep+=word
            k+=1
        return k        