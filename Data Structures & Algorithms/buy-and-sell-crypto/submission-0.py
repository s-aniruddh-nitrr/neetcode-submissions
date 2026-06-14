class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = []
        for i in range(len(prices)):
            max_right = 0
            for j in range(i+1, len(prices)):
                max_right = max(max_right, prices[j])
            result.append(max_right-prices[i])
        print(result)
        if max(result)<0:
            return 0
        return max(result)
        