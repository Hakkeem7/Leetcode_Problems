class Solution:
    def reverseString(self, s: List[str]) -> None:
        str=[]
        s.reverse()
        str.append(s)
        return str

        