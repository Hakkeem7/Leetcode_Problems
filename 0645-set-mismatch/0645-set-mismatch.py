class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen={}
        duplicate=-1
        for num in nums:
            if num in seen:
                duplicate=num
            else:
                seen[num]=1
        exp_num=n*(n+1)//2
        actual_num=sum(seen)
        missing=exp_num-actual_num

        return [duplicate,missing]
        