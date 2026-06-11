class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = defaultdict(int)
        for i in nums:
            map1[i] +=1
        list1 = [[] for _ in range(len(nums) + 1)]
        for key, value in map1.items():
            list1[value].append(key)
        print(list1)
        list1.reverse()
        print(list1)
        result = list()
        for i in range(len(list1)):
            if list1[i]:
                result.extend(list1[i])
        print (result)
        return result[:k]