class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map1 = defaultdict(int)
        for i in nums:
            map1[i] += 1
        sorted_map = dict()
        sorted_map = sorted(map1.items(), key=lambda x: x[1], reverse = True)
        list1 = list()
        for key,value in sorted_map:
            list1.append(key)
        return list1[:k]
                 