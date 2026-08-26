class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        rep=""
        count=0
        while len(rep)<len(b):
            rep+=a
            count+=1
        if b in rep:
            return count
        rep+=a
        count+=1
        if b in rep:
            return count
        return -1