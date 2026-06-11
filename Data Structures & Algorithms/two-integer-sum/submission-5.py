class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i,val in enumerate(nums):
            if(target-val) in result:
                return [result[target-val], i]
            result[val]=i

        