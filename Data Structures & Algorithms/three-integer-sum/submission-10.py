class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        map1 = defaultdict(int)        
        part_of_result = []
        
        for i in nums:
            map1[i]+=1 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = -(nums[i]+nums[j])
                map1[nums[i]]-=1
                map1[nums[j]]-=1
                tuple1 = ()
                if( target in map1 and ((map1.get(target))>0)):
                    print(nums[i],nums[j], target)
                    temp = tuple(sorted([nums[i], nums[j], target]))
                    tuple1 = tuple1 + temp
                    if tuple1 not in part_of_result:
                        part_of_result.append(tuple1)
                    #print("part_of_result", part_of_result)
                map1[nums[i]]+=1
                map1[nums[j]]+=1
        return part_of_result

         













