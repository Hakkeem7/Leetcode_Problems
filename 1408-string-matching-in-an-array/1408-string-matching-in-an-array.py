class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result=[]
        for i,w in enumerate(words):
            for j,aw in enumerate(words):
                if i!=j and w in aw:
                    result.append(w)
                    break
        return result



        