class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_multiple = [1]*len(nums)
        left_multiple = [1]*len(nums)
        for i in range(1,len(nums)):
            multiple = 1
            for j in range(i, len(nums)):
                multiple = multiple * nums[j]
            right_multiple[i-1] = multiple
        print(right_multiple)
        for i in range(0,len(nums)):
            multiple = 1
            for j in range(i):
                multiple = multiple * nums[j]
            left_multiple[i] = multiple
        print(left_multiple)
        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] = left_multiple[i] * right_multiple[i] 
        return result

        