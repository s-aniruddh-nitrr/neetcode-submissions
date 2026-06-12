class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set1 =  {2, 3, 4, 5, 10, 20}
        res = 0
        set1 = set(nums)

        for num in nums:
            curr = num
            streak = 0
            while curr in set1:
                curr+=1
                streak+=1
                res = max(res, streak )
        return res