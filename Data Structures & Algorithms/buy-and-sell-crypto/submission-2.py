class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_left = prices[0]
        list1 = [0]
        for i in range(1, len(prices)):
            min_left = min(min_left, prices[i])
            list1.append(prices[i]-min_left)
        print(list1)
        return(max(list1))