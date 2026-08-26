class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,j in enumerate(nums):
            store = target-j
            if store in dict:
                return dict[store],i
            dict[j]=i



