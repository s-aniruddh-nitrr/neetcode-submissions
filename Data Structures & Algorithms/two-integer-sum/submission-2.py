class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[j] == target-nums[i]):
                    result.append(i)
                    result.append(j)
                    return result
        result.append(1)
        result.append(2)
        return result