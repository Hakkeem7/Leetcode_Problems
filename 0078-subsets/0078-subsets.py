class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def back(i,current):
            if i==len(nums):
                result.append(current[:])
                return
            # dont take the element
            back(i+1,current)
            
            #take the element
            current.append(nums[i])
            back(i+1,current)
            
            # remove element
            current.pop()
        back(0,[])
    
        return result
        