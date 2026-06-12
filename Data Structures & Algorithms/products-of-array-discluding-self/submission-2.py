class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result =[0]*len(nums) 
        right_list = [0]*len(nums)
        all_multiple = 1
        cc = -1
        dd = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                all_multiple = all_multiple * nums[i]
            else:
                dd+=1
                cc = i
        if(dd>1):
            return result
        for i in range(len(nums)):
            if(nums[i]!=0):
                right_list[i] = all_multiple//nums[i]
            else:
                right_list[i] = all_multiple
        if cc>0:
            result[cc]  = all_multiple
            return result    
        return right_list