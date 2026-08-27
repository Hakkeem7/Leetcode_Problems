class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
    
        i=0
        h=len(s)-1
        while i<h:
            s[i],s[h]=s[h],s[i]
            i+=1
            h-=1
        return s
